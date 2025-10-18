# user_data - Instructions et exemples pour Freqtrade

Ce répertoire (`user_data`) contient la configuration et les données persistantes utilisées par le container Freqtrade.

Structure recommandée

- `config.json` - fichier de configuration principal (copier depuis `config.example.json`)
- `strategies/` - dossier pour vos stratégies Python (ex: `SampleStrategy.py`)
- `logs/` - fichiers de logs (générés par le container)
- `freqtrade.sqlite` - base de données SQLite (générée par le container)

Exemple d'initialisation

1. Copier le template de configuration :

```bash
cp config.example.json config.json
```

2. Éditer `config.json` et renseigner vos clés d'API (si vous tradez live). Gardez `dry_run: true` tant que vous testez.

3. Créer les dossiers nécessaires (si le dossier monté depuis l'hôte est vide) :

```bash
mkdir -p strategies logs
# Assurez-vous que le propriétaire/propriétés conviennent pour Docker
# Ex: chown -R $USER:docker ./user_data  (adapter selon votre environnement)
```

Où placer vos stratégies

- Déposez vos fichiers de stratégie Python dans `strategies/`.
- Exemple minimal : `strategies/SampleStrategy.py`.
- Dans `config.json`, réglez `strategy` ou indiquez la stratégie via la ligne de commande `--strategy`.

Sécurité des clés

- Ne commitez jamais vos clés API dans le dépôt.
- Utilisez des variables d'environnement ou des secrets pour stocker vos clés si possible.
- Exemple pour masquer la clé : éditez `config.json` localement et ajoutez le fichier au `.gitignore`.

Démarrer avec Docker Compose

Depuis le dossier `axoide-freqtrade` :

```bash
# Optionnel: définir APP_DATA_DIR si vous stockez ailleurs
export APP_DATA_DIR=$(pwd)
# Lancer les services
docker compose up -d
# Voir les logs
docker compose logs -f freqtrade
```

Tips

- Keep `dry_run: true` until confident with strategy.
- Use a dedicated exchange sub-account for live trading.
- Backup `freqtrade.sqlite` regularly.

Support et debug

- Si le container ne démarre pas, inspectez `docker compose ps` puis `docker logs freqtrade`.
- Healthcheck HTTP: le service expose le port 8080 pour l'API / Web UI.

---

Fichier créé automatiquement par l'outil d'aide. Adaptez selon vos besoins.