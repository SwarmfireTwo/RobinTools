import json
with open('Componentes/Secrets/Secrets.json', 'r') as secrets_json:
    SecretsJson = json.load(secrets_json)
    # Declaração de variáveis
    TokenRobinDoHood = str(SecretsJson["TokenRobinDoHood"])
    IdServerOficial = int(SecretsJson["IdServerOficial"])
    IdServerTeste = int(SecretsJson["IdServerTeste"])
    IdChannelLogs = int(SecretsJson["IdChannelLogs"])
    IdContaSwarmfire = int(SecretsJson["IdContaSwarmfire"])
    IdContaDevpobrerico = int(SecretsJson["IdContaDevpobrerico"])
    
    # Verificação se os dados foram encontrados e carregados
    if IdContaSwarmfire != 484053771203379210:
        print('Inconsistência nos dados das Secrets, parando aplicação.')
        exit()
    
    secrets_json.close()