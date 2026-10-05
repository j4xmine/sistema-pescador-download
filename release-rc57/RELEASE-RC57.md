# Sistema Pescador RC57.3 — GuiaBridge 0.5.58 validado

Atualização autorizada após validação operacional de sete guias na versão 0.5.58 em 05/10/2026: sete PDFs validados, uma autenticação e logout confirmado. Processamento do lote em 13min52s, sem promessa de redução de tempo do eSocial.

Mantém as funções da RC57.2 e inclui o GuiaBridge 0.5.58: mesma aba e sessão durante o lote, cache preservado, preenchimento direto validado, ordem decrescente, navegador oculto e conferências de CPF, competência, valor e encerramento. Remove uma leitura redundante na retomada de alteração já salva. Bloqueia apenas quatro imagens decorativas.

Não inclui o novo módulo de requerimento do seguro-defeso/MTE. Não exige alteração no backend.

Aguarde as emissões terminarem, feche o Sistema Pescador e execute o instalador sem desinstalar. O instalador preserva dados e configurações, cria backup do GuiaBridge e impede atualização do aplicativo quando o componente falha. O pacote passa pelos testes do atualizador e do instalador antes de ser disponibilizado no catálogo público.

## Integridade e liberação

Compilação e testes do instalador concluídos com sucesso no [GitHub Actions](https://github.com/j4xmine/sistema-pescador-frontend/actions/runs/37269695899). O pacote unificado foi recompilado para incorporar o GuiaBridge 0.5.58 já validado em uso real; a publicação pública transfere esse pacote sem nova recompilação.

SHA-256 do instalador: `d97068f6867d535cedcc74b63c4cc8c6ec5e07a56e9206a463bff8b1fdaf118e`.
