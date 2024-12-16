# Generazione e Trasformazione di Audio per Dataset di Comandi Vocali

## Descrizione del Progetto
Questo progetto ha come obiettivo la generazione e la trasformazione di file audio contenenti comandi vocali. Utilizzando una combinazione di sintetizzazione vocale tramite **gTTS** (Google Text-to-Speech) e manipolazioni audio con **pydub**, il sistema genera dataset diversificati per addestrare modelli di riconoscimento vocale.

---

## Funzionalità Principali
1. **Generazione di comandi vocali**: Produzione di file audio per comandi vocali specifici, come "su", "sinistra", ecc., in formato `.wav`.
2. **Trasformazioni audio**: Applicazione di modifiche casuali alla velocità, al pitch, al volume e alla durata (taglio) per creare variazioni realistiche dei file vocali.
3. **Silenzio generato**: Creazione di file `.wav` contenenti silenzi per bilanciare il dataset.
4. **Supporto multilingua**: Possibilità di specificare la lingua del testo (attualmente configurato per l'italiano).

---

## Struttura del Progetto
### File Principali
- **`generasample.py`**: Script principale per la generazione e trasformazione dell'audio. Contiene:
  - La funzione `apply_transformations` per modificare l'audio.
  - La funzione `generate_audio` per sintetizzare e salvare i comandi vocali.
  - La funzione `generate_silence` per creare file di silenzio.
- **Modello preaddestrato**:
  - **`simple_model.pth`**: File del modello neurale per il riconoscimento vocale (potrebbe richiedere ulteriori dettagli sul suo utilizzo).
- **File audio**:
  - **`rec.wav`**: Un file audio registrato (probabilmente usato per test o addestramento).
  - Altri file `.mp3` (`destr.mp3`, `snistra.mp3`, `snistra2.mp3`, `suu.mp3`): File audio sorgenti o trasformati.

---

## Dipendenze
Assicurati di avere i seguenti pacchetti installati:
- **gTTS** (Google Text-to-Speech): `pip install gtts`
- **pydub**: `pip install pydub`
- **ffmpeg**: Necessario per la manipolazione audio con pydub. Installabile tramite gestori di pacchetti del sistema operativo.
- **requirements.txt**: File contenente le dipendenze del progetto.
   ```bash
   pip install -r requirements.txt
   ```

---

## Esecuzione per creare samples
### Passaggi per Generare il Dataset
1. **Configurazione comandi**:
   Modifica la lista `commands` nello script `generaSample.py` per includere i comandi desiderati.
   ```python
   commands = ["destra", "sinistra", "su", "giù"]
   ```
2. **Esecuzione dello script**:
   Avvia il file `generasample.py` per generare il dataset. I file generati verranno salvati nella cartella `test_dataset`.
   ```bash
   python generaSample.py
   ```
3. **File generati**:
   - Comandi vocali con varianti trasformate.
   - File di silenzio per bilanciare il dataset.

## Esecuzione per testare prediction
### Passaggi per Testare il modello
1. **Aprire file audio.ipynb**
2. **Leggere all'interno, c'è tutto spiegato**:
   - Test con modello trainato da me
   - Test con modello pretrainato online

---

## Personalizzazioni
### Parametri di Trasformazione
Puoi regolare i seguenti parametri nella funzione `generate_audio` per personalizzare le trasformazioni:
- **Velocità (`speed_prob`)**: Probabilità di modificare la velocità (default: 70%).
- **Pitch (`pitch_prob`)**: Probabilità di modificare il pitch (default: 30%).
- **Volume (`volume_prob`)**: Probabilità di cambiare il volume (default: 50%).
- **Taglio (`random_cut_prob`)**: Probabilità di effettuare un taglio casuale nell'audio (default: 30%).

---

## Applicazioni
- Addestramento di modelli di riconoscimento vocale.
- Test e validazione di sistemi basati su comandi vocali.
- Generazione di dataset diversificati per scenari di machine learning.

---

Created by fumaghe