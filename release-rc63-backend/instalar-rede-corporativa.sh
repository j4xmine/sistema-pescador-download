#!/usr/bin/env bash
set -Eeuo pipefail
umask 077
[[ $EUID -eq 0 ]] || { echo 'Execute com sudo.' >&2; exit 1; }
pacote=${1:?Informe o JAR verificado.}
destino=/opt/sistema-pescador/sistema-pescador.jar
servico=sistema-pescador.service
esperado_novo=7d364f1331cc99374900766d1a7a8c8a19058d03bb6cc28e768a3e376e4aeb66
esperado_atual=31c900b1dc5359ff94e1e35bf6c87e6dc8dc66127e3f7f354869d09889e45728
[[ -f "$pacote" && -f "$destino" && ! -L "$destino" ]] || { echo 'Arquivo ou destino inesperado.' >&2; exit 1; }
command -v curl >/dev/null
command -v flock >/dev/null
exec 9>/opt/sistema-pescador/.atualizacao-assistente.lock
flock -n 9 || { echo 'Outra atualizacao esta em andamento.' >&2; exit 1; }
[[ $(sha256sum "$pacote" | cut -d' ' -f1) == "$esperado_novo" ]] || { echo 'Pacote divergente.' >&2; exit 1; }
atual=$(sha256sum "$destino" | cut -d' ' -f1)
if [[ "$atual" == "$esperado_novo" ]]; then echo 'REDE_CORPORATIVA_JA_INSTALADA=True'; systemctl is-active "$servico"; exit 0; fi
[[ "$atual" == "$esperado_atual" ]] || { echo 'Backend instalado diferente do Agenda Compartilhada RC60 verificado. Nada foi alterado.' >&2; exit 1; }
systemctl is-active --quiet "$servico" || { echo 'Servico nao esta ativo; nada foi alterado.' >&2; exit 1; }
mkdir -p /opt/sistema-pescador/backups
backup=$(mktemp -d /opt/sistema-pescador/backups/pre-rede-corporativa-XXXXXXXX)
cp --preserve=all "$destino" "$backup/sistema-pescador.jar"
systemctl cat "$servico" > "$backup/servico.txt"
[[ $(sha256sum "$backup/sistema-pescador.jar" | cut -d' ' -f1) == "$esperado_atual" ]]
estagio=$(mktemp /opt/sistema-pescador/.backend-rede-corporativa-XXXXXXXX.jar)
cp --preserve=all "$destino" "$estagio"
cat "$pacote" > "$estagio"
[[ $(sha256sum "$estagio" | cut -d' ' -f1) == "$esperado_novo" ]]
dropin=/etc/systemd/system/sistema-pescador.service.d/99-rede-corporativa.conf
[[ ! -L "$dropin" ]] || { echo 'Configuracao inesperada.' >&2; exit 1; }
if [[ -f "$dropin" ]]; then cp --preserve=all "$dropin" "$backup/rede-dropin.conf"; fi
parado=false
substituido=false
restaurar() {
  codigo=$?
  trap - EXIT
  rm -f "$estagio"
  if [[ $codigo -ne 0 && "$parado" == true ]]; then
    if [[ "$substituido" == true ]]; then
      systemctl stop "$servico" || true
      cp --preserve=all "$backup/sistema-pescador.jar" "$destino"
    fi
    if [[ -f "$backup/rede-dropin.conf" ]]; then cp --preserve=all "$backup/rede-dropin.conf" "$dropin"; else rm -f "$dropin"; fi
    systemctl daemon-reload
    systemctl start "$servico" || true
    echo "ATUALIZACAO_FALHOU_BACKUP=$backup" >&2
  fi
  exit "$codigo"
}
trap restaurar EXIT
parado=true
systemctl stop "$servico"
mv -f "$estagio" "$destino"
substituido=true
mkdir -p "$(dirname "$dropin")"
printf '[Service]\nEnvironment=REDE_CORPORATIVA_HABILITADA=true\n' > "$dropin"
chmod 600 "$dropin"
systemctl daemon-reload
systemctl start "$servico"
pronto=false
for tentativa in $(seq 1 45); do
  status=$(curl --silent --output /dev/null --write-out '%{http_code}' --connect-timeout 2 --max-time 3 http://127.0.0.1:8080/usuarios/me || true)
  pagina=$(curl --silent --output /dev/null --write-out '%{http_code}' --connect-timeout 2 --max-time 3 http://127.0.0.1:8080/foto-online/ || true)
  if [[ "$status" == 401 && "$pagina" == 200 ]] && systemctl is-active --quiet "$servico"; then pronto=true; break; fi
  sleep 2
done
[[ "$pronto" == true ]] || { echo 'API nao confirmou inicializacao; restaurando JAR anterior.' >&2; exit 1; }
printf 'REDE_CORPORATIVA_BACKEND_INSTALADO=True\nAPI_AUTENTICADA_401=True\nPAGINA_CAPTURA_200=True\nREDE_CORPORATIVA_HABILITADA=True\nCONFIGURACOES_MFA_NAO_ALTERADAS=True\nBACKUP=%s\n' "$backup"
