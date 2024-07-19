# F-Monitor

| Language |
|----------|
| Français |
| English  |

## Français

F-Monitor est un script Python conçu pour surveiller une URL en envoyant des pings à intervalles réguliers. Ce script est particulièrement utile pour vérifier la disponibilité d'un site web ou d'un service en temps réel comme un bot WhatsApp par exemple.

### Fonctionnalités

- **Ping régulier** : Envoie des requêtes HTTP à une URL spécifiée à intervalles réguliers.
- **Surveillance en arrière-plan** : Utilise `termux-job-scheduler` pour s'exécuter même si Termux est fermé.

### Prérequis

- **Termux** : Un environnement de terminal pour Android.
- **Termux:API** : Une application nécessaire pour utiliser les commandes `termux-api`.
- **Python** : Le langage de programmation utilisé pour le script.
- **Bibliothèques Python** : `requests` pour envoyer des requêtes HTTP.

### Installation

1. **Installer Termux** :
   - Téléchargez et installez Termux depuis le Google Play Store ou F-Droid.

2. **Installer Termux:API** :
   - Téléchargez et installez l'application Termux:API depuis le Google Play Store ou F-Droid.

3. **Installer Python et les bibliothèques nécessaires** :
   ```sh
   pkg install python termux-api
   pip install requests
   ```

4. **Télécharger le script** :
   - Téléchargez ou clonez ce dépôt sur votre appareil.

### Utilisation

1. **Ouvrir Termux** :
   - Ouvrez l'application Termux sur votre appareil.

2. **Naviguer vers le répertoire du script** :
   ```sh
   cd f-monitor
   ```

3. **Exécuter le script** :
   ```sh
   python f-monitor.py <url>
   ```
   Remplacez `<url>` par l'URL que vous souhaitez surveiller.

   Par exemple :
   ```sh
   python f-monitor.py https://www.example.com
   ```

4. **Vérifier la sortie** :
   - Le script affichera les résultats des pings à l'URL spécifiée toutes les minutes.

### Personnalisation

- **Intervalle de ping** : Le script est configuré pour envoyer des pings toutes les minutes. Si vous souhaitez modifier cet intervalle, vous pouvez ajuster la valeur de `time.sleep(60)` dans le script.

### Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

### Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## English

F-Monitor is a Python script designed to monitor a URL by sending pings at regular intervals. This script is particularly useful for checking the availability of a website or service in real-time, such as a WhatsApp bot for example.

### Features

- **Regular Ping** : Sends HTTP requests to a specified URL at regular intervals.
- **Background Monitoring** : Uses `termux-job-scheduler` to run even if Termux is closed.

### Prerequisites

- **Termux** : A terminal environment for Android.
- **Termux:API** : An application necessary for using `termux-api` commands.
- **Python** : The programming language used for the script.
- **Python Libraries** : `requests` to send HTTP requests.

### Installation

1. **Install Termux** :
   - Download and install Termux from the Google Play Store or F-Droid.

2. **Install Termux:API** :
   - Download and install the Termux:API application from the Google Play Store or F-Droid.

3. **Install Python and necessary libraries** :
   ```sh
   pkg install python termux-api
   pip install requests
   ```

4. **Download the script** :
   - Download or clone this repository to your device.

### Usage

1. **Open Termux** :
   - Open the Termux application on your device.

2. **Navigate to the script directory** :
   ```sh
   cd f-monitor
   ```

3. **Run the script** :
   ```sh
   python f-monitor.py <url>
   ```
   Replace `<url>` with the URL you want to monitor.

   For example :
   ```sh
   python f-monitor.py https://www.example.com
   ```

4. **Check the output** :
   - The script will display the results of the pings to the specified URL every minute.

### Customization

- **Ping Interval** : The script is configured to send pings every minute. If you wish to modify this interval, you can adjust the value of `time.sleep(60)` in the script.

### Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
