# coding:utf8

"""Italian dictionary"""

it = {
    "LANGUAGE" : u"Italiano",

    # Client notifications
    "config-cleared-notification" : u"Impostazioni resettate. I cambiamenti saranno memorizzati quando salverai una configurazione valida.",

    "relative-config-notification" : u"Caricato i file di configurazione relativi: {}",

    "connection-attempt-notification" : u"Tentativo di connessione a {}:{}",  # Port, IP
    "reconnection-attempt-notification" : u"Connessione col server persa, tentativo di riconnesione in corso",
    "disconnection-notification" : u"Disconnesso dal server",
    "connection-failed-notification" : u"Connessione col server fallita",
    "connected-successful-notification" : u"Connessione al server effettuata con successo",
    "retrying-notification" : u"%s, Nuovo tentativo in %d secondi...",  # Seconds

    "rewind-notification" : u"Riavvolgendo a causa della differenza temporale con {}",  # User
    "fastforward-notification" : u"Avanzamento rapido a causa della differenza temporale con {}",  # User
    "slowdown-notification" : u"Rallentando a causa della differenza temporale con {}",  # User
    "revert-notification" : u"Ritornando alla velocità di riproduzione normale",

    "pause-notification" : u"{} ha messo in pausa",  # User
    "unpause-notification" : u"{} ha ripreso la riproduzione",  # User
    "seek-notification" : u"{} è passato da {} a {}",  # User, from time, to time

    "current-offset-notification" : u"Offset corrente: {} secondi",  # Offset

    "media-directory-list-updated-notification" : u"Le cartelle media di Syncplay sono state aggiornate.",

    "room-join-notification" : u"{} è entranto nella stanza: '{}'",  # User
    "left-notification" : u"{} ha abbandonato",  # User
    "left-paused-notification" : u"{} ha abbandonato, {} ha messo in pausa",  # User who left, User who paused
    "playing-notification" : u"{} sta riproducendo '{}' ({})",  # User, file, duration
    "playing-notification/room-addendum" :  u" nella stanza: '{}'",  # Room

    "not-all-ready" : u"Non pronti: {}", # Usernames
    "all-users-ready" : u"Tutti i partecipanti sono pronti ({} utenti)", #Number of ready users
    "ready-to-unpause-notification" : u"Ora sei pronto - premi ancora una volta il tasto pausa per riprendere la riproduzione",
    "set-as-ready-notification" : u"Ora sei pronto",
    "set-as-not-ready-notification" : u"Non sei pronto",
    "autoplaying-notification" : u"Riproduzione automatica in {}...",  # Number of seconds until playback will start

    "identifying-as-controller-notification" : u"Identificato come gestore della stanza con password '{}'...",
    "failed-to-identify-as-controller-notification" : u"{} ha fallito l'identificazione come gestore della stanza.",
    "authenticated-as-controller-notification" : u"{} autenticato come gestore della stanza",
    "created-controlled-room-notification" : u"Stanza gestita '{}' creata con password '{}'. Per favore salva queste informazioni per futura consultazione!", # RoomName, operatorPassword

    "file-different-notification" : u"Il file che stai riproducendo sembra essere diverso da quello di {}",  # User
    "file-differences-notification" : u"Il tuo file possiede le seguenti differenze: {}", # Differences
    "room-file-differences" : u"Differenze nel tuo file: {}", # File differences (filename, size, and/or duration)
    "file-difference-filename" : u"nome",
    "file-difference-filesize" : u"dimensione",
    "file-difference-duration" : u"durata",
    "alone-in-the-room": u"Non ci sono altri utenti nella stanza",

    "different-filesize-notification" : u" (la dimensione del tuo file è diversa da quella degli altri partecipanti!)",
    "userlist-playing-notification" : u"{} sta riproducendo:", #Username
    "file-played-by-notification" : u"File: {} è in riproduzione da:",  # File
    "no-file-played-notification" : u"{} non sta riproducendo alcun file", # Username
    "notplaying-notification" : u"Partecipanti che non stanno riproducendo alcun file:",
    "userlist-room-notification" :  u"Nella stanza '{}':",  # Room
    "userlist-file-notification" : u"File",
    "controller-userlist-userflag" : u"Gestore",
    "ready-userlist-userflag" : u"Pronto",

    "update-check-failed-notification" : u"Controllo automatico degli aggiornamenti di Syncplay {} fallito. Vuoi visitare http://syncplay.pl/ per verificare manualmente la presenza di aggiornamenti?", #Syncplay version
    "syncplay-uptodate-notification" : u"Syncplay è aggiornato",
    "syncplay-updateavailable-notification" : u"Nuova versione di Syncplay disponibile. Vuoi visitare la pagina delle release?",

    "mplayer-file-required-notification" : u"Utilizzare Syncplay con mplayer richiede la selezione del file all'avvio",
    "mplayer-file-required-notification/example" : u"Esempio di utilizzo: syncplay [opzioni] [url|percorso/]nomefile",
    "mplayer2-required" : u"Syncplay non è compatibile con MPlayer 1.x, per favore utilizza mplayer2 or mpv",

    "unrecognized-command-notification" : u"Comando non riconosciuto",
    "commandlist-notification" : u"Comandi disponibili:",
    "commandlist-notification/room" : u"\tr [nome] - cambia stanza",
    "commandlist-notification/list" : u"\tl - mostra la lista di utenti",
    "commandlist-notification/undo" : u"\tu - annulla l'ultima ricerca",
    "commandlist-notification/pause" : u"\tp - attiva o disattiva la pausa",
    "commandlist-notification/seek" : u"\t[s][+-]tempo - seek to the given value of time, if + or - is not specified it's absolute time in seconds or min:sec",
    "commandlist-notification/help" : u"\th - questo help",
    "commandlist-notification/toggle" : u"\tt - attiva o disattiva lo stato 'Pronto'",
    "commandlist-notification/create" : u"\tc [nome] - crea una stanza gestita usando il nome della stanza attuale",
    "commandlist-notification/auth" : u"\ta [password] - autentica come gestore della stanza, utilizzando la password del gestore",
    "commandlist-notification/chat" : u"\tch [message] - invia un messaggio nella chat della stanza",
    "syncplay-version-notification" : u"Versione di Syncplay: {}",  # syncplay.version
    "more-info-notification" : u"Maggiori informazioni a: {}",  # projectURL

    "gui-data-cleared-notification" : u"Syncplay ha resettato i dati, usati dalla GUI, relativi ai percorsi ed allo stato delle finestre.",
    "language-changed-msgbox-label" : u"La lingua sarà cambiata quando avvierai Syncplay.",
    "promptforupdate-label" : u"Ti piacerebbe che, di tanto in tanto, Syncplay controllasse automaticamente la presenza di aggiornamenti?",

    "vlc-interface-version-mismatch": u"Stai eseguendo la versione {} del modulo di interfaccia per VLC di Syncplay, ma Syncplay è progettato per essere utilizzato con la versione {} o superiore. Per favore, fai riferimento alla User Guide di Syncplay presso http://syncplay.pl/guide/ per istruzioni su come installare syncplay.lua.",  # VLC interface version, VLC interface min version
    "vlc-interface-oldversion-warning": u"Attenzione: Syncplay ha rilevato una vecchia versione del modulo di interfaccia per VLC di Syncplay installata nella cartella di VLC. Per favore, fai riferimento alla User Guide di Syncplay presso http://syncplay.pl/guide/ per istruzioni su come installare syncplay.lua.",
    "media-player-latency-warning": u"Attenzione: il media player ha impiegato {} secondi per rispondere. Se stai avendo problemi di sincronizzazione, chiudi delle applicazioni per liberare le risorse di sistema e, se ciò non dovesse avere alcun effetto, prova un altro media player.", # Seconds to respond
    "vlc-interface-not-installed": u"Attenzione: il modulo di interfaccia per VLC di Syncplay non è stato trovato nella cartella di VLC. Se stai utilizzando VLC 2.0, VLC userà il modulo syncplay.lua contenuto nella cartella di Syncplay, ma ciò significa che altri custom script di interfaccia ed estensioni non funzioneranno. Per favore, fai riferimento alla User Guide di Syncplay presso http://syncplay.pl/guide/ per istruzioni su come installare syncplay.lua.",
    "mpv-unresponsive-error": u"mpv non ha risposto per {} secondi, quindi sembra non funzionare correttamente. Per favore, riavvia Syncplay.", # Seconds to respond

    # Client prompts
    "enter-to-exit-prompt" : u"Premi Invio per uscire\n",

    # Client errors
    "missing-arguments-error" : u"Alcuni argomenti obbligatori non sono stati trovati. Fai riferimento a --help",
    "server-timeout-error" : u"Connessione col server scaduta",
    "mpc-slave-error" : u"Non è possibile avviare MPC in modalità slave!",
    "mpc-version-insufficient-error" : u"Versione di MPC non sufficiente, per favore usa `mpc-hc` >= `{}`",
    "mpc-be-version-insufficient-error" : u"Versione di MPC non sufficiente, per favore usa `mpc-be` >= `{}`",
    "mpv-version-error" : u"Syncplay non è compatibile con questa versione di mpv. Per favore usa un'altra versione di mpv (es. Git HEAD).",
    "player-file-open-error" : u"Il player non è riuscito ad aprire il file",
    "player-path-error" : u"Il path del player non è configurato correttamente. I player supportati sono: mpv, VLC, MPC-HC, MPC-BE e mplayer2",
    "hostname-empty-error" : u"Hostname non può essere vuoto",
    "empty-error" : u"{} non può esssere vuoto",  # Configuration
    "media-player-error": u"Errore media player: \"{}\"",  # Error line
    "unable-import-gui-error": u"Non è possibile importare le librerie GUI. Hai bisogno di PySide per poter utilizzare la GUI.",

    "arguments-missing-error" : u"Alcuni argomenti obbligatori non sono stati trovati. Fai riferimento a --help",

    "unable-to-start-client-error" : u"Impossibile avviare il client",

    "player-path-config-error": u"Il path del player non è configurato correttamente. I player supportati sono: mpv, VLC, MPC-HC, MPC-BE e mplayer2.",
    "no-file-path-config-error" :u"Deve essere selezionato un file prima di avviare il player",
    "no-hostname-config-error": u"Hostname non può essere vuoto",
    "invalid-port-config-error" : u"La porta deve essere valida",
    "empty-value-config-error" : u"{} non può essere vuoto", # Config option

    "not-json-error" : u"Non è una stringa con codifica JSON\n",
    "hello-arguments-error" : u"Argomenti Hello non sufficienti\n",
    "version-mismatch-error" : u"La versione del client è diversa da quella del server\n",
    "vlc-failed-connection": u"Impossibile collegarsi a VLC. Se non hai installato syncplay.lua e stai usando l'ultima versione di VLC, fai riferimento a http://syncplay.pl/LUA/ per istruzioni.",
    "vlc-failed-noscript": u"VLC ha segnalato che lo script di interfaccia syncplay.lua non è stato installato. Per favore, fai riferimento a http://syncplay.pl/LUA/ per istruzioni.",
    "vlc-failed-versioncheck": u"Questa versione di VLC non è supportata da Syncplay.",

    "feature-sharedPlaylists" : u"playlist condivise", # used for not-supported-by-server-error
    "feature-chat" : u"chat", # used for not-supported-by-server-error
    "feature-readiness" : u"prontezza", # used for not-supported-by-server-error
    "feature-readiness" : u"prontezza", # used for not-supported-by-server-error # TODO needs to be reviewed
    "feature-managedRooms" : u"stanze gestite", # used for not-supported-by-server-error

    "not-supported-by-server-error" : u"La feature {} non è supportata da questo server..", #feature
    "shared-playlists-not-supported-by-server-error" : u"La feature playlist condivise potrebbe non essere supportata dal server. Si necessita di un server avente Syncplay {}+ per assicurarsi che essa funzioni correttamente, tuttavia il server sta utilizzando Syncplay {}.", #minVersion, serverVersion
    "shared-playlists-disabled-by-server-error" : u"La feature playlist condivise è stata disabilitata nella configurazione del server. Per utilizzarla, dovrai collegarti ad un altro server.",

    "invalid-seek-value" : u"Valore di ricerca non valido",
    "invalid-offset-value" : u"Valore di offset non valido",

    "switch-file-not-found-error" : u"Impossibile passare al file '{0}'. Syncplay analizza le cartelle media specificate.", # File not found
    "folder-search-timeout-error" : u"La ricerca nelle cartelle media è stata interrotta siccome l'analisi di '{}' sta impiegando troppo tempo. Ciò accade se si aggiunge una cartella con troppe sottocartelle nella lista di ricerca. Per riabilitare la selezione automatica dei file seleziona File->Imposta Cartelle Media nella barra dei menù e rimuovi questa cartella o sostituiscila con una sottocartella appropriata. Se la cartella è idonea, è possibile riabilitarla selezionando File->Imposta Cartelle Media e premendo 'OK'.", #Folder
    "folder-search-first-file-timeout-error" : u"La ricerca dei media in '{}' è stata interrotta siccome l'accesso alla cartella sta impiegando troppo tempo. Ciò accade se essa è un disco di rete oppure se hai impostato il blocco della rotazione del disco rigido dopo un certo periodo di inattività. Per riabilitare la selezione automatica dei file seleziona File->Imposta Cartelle Media, quindi rimuovi la cartella oppure risolvi il problema (es. cambiando le impostazioni del risparmio energetico).", #Folder
    "added-file-not-in-media-directory-error" : u"Hai selezionato un file in '{}'. Essa non è una cartella media conosciuta. Puoi aggiungerla come cartella media selezionando File->Imposta Cartella Media nella barra dei menù.", #Folder
    "no-media-directories-error" : u"Nessuna cartella media è stata configurata. Per permette il corretto funzionamento delle feature playlist condivise e selezione automatica del file, naviga in File->Imposta Cartelle Media e specifica dove Syncplay debba ricercare i file media.",
    "cannot-find-directory-error" : u"Impossibile trovare la cartella media '{}'. Per aggiornare la lista delle cartelle media seleziona File->Imposta Cartelle Media dalla barra dei menù e specifica dove Syncplay debba ricercare i file media.",

    "failed-to-load-server-list-error" : u"Impossibile caricare la lista dei server pubblici. Per favore, visita http://www.syncplay.pl/ col tuo browser.",

    # Client arguments
    "argument-description" : 'Soluzione per sincronizzare la riproduzione di istanze di media player multiple attraverso la rete.',
    "argument-epilog" : 'Se non è specificata alcuna opzione saranno utilizzati i valori _config ',
    "nogui-argument" : 'non mostrare la GUI',
    "host-argument" : 'indirizzo del server',
    "name-argument" : 'username desiderato',
    "debug-argument" : 'modalità debug',
    "force-gui-prompt-argument" : 'mostra il prompt di configurazione',
    "no-store-argument" : 'non salva i valori in .syncplay',
    "room-argument" : 'stanza di default',
    "password-argument" : 'password del server',
    "player-path-argument" : 'percorso dell\'eseguibile del tuo player',
    "file-argument" : 'file da riprodurre',
    "args-argument" : 'opzioni del player, se hai bisogno di passare opzioni che iniziano con - anteponile con un singolo \'--\'',
    "clear-gui-data-argument" : 'resetta il percorso e i dati inerenti allo stato della GUI salvati come QSettings',
    "language-argument" :'lingua per i messaggi di Syncplay (de/en/ru)',

    "version-argument" : 'mostra la tua versione',
    "version-message" : u"Stai usando la versione di Syncplay {} ({})",

    # Client labels
    "config-window-title" : u"Configurazione di Syncplay",

    "connection-group-title" : u"Impostazioni di connessione",
    "host-label" : u"Indirizzo del server: ",
    "name-label" :  u"Username (opzionale):",
    "password-label" :  u"Password del server(se necessaria):",
    "room-label" : u"Stanza di default: ",

    "media-setting-title" : u"Impostazioni del media player",
    "executable-path-label" : u"Percorso del media player:",
    "media-path-label" : u"Percorso del video (opzionale):",
    "player-arguments-label" : u"Argomenti del player (se necessari):",
    "browse-label" : u"Sfoglia",
    "update-server-list-label" : u"Aggiorna lista",

    "more-title" : u"Mostra altre impostazioni",
    "never-rewind-value" : u"Mai",
    "seconds-suffix" : u" secs",
    "privacy-sendraw-option" : u"Invio semplice",
    "privacy-sendhashed-option" : u"Invio criptato",
    "privacy-dontsend-option" : u"Non inviare",
    "filename-privacy-label" : u"Nome del file:",
    "filesize-privacy-label" : u"Dimensione del file:",
    "checkforupdatesautomatically-label" : u"Controlla automaticamente gli aggiornamenti di Syncplay",
    "slowondesync-label" : u"Rallenta in caso di desync minimo (non supportato su MPC-HC/BE)",
    "rewindondesync-label" : u"Riavvolgi in caso di desync grave (consigliato)",
    "fastforwardondesync-label" : u"Avanzamento rapido in caso di ritardo (consigliato)",
    "fastforwardondesync-label" : u"Avanzamento rapido in caso di lag (consigliato)",
    "dontslowdownwithme-label" : u"Non rallentare o riavvolgere gli altri utenti (sperimentale)",
    "pausing-title" : u"In pausa",
    "pauseonleave-label" : u"In pausa quando gli utenti abbandonano (es. disconnessione)",
    "readiness-title" : u"Stato iniziale di Pronto",
    "readyatstart-label" : u"Impostami sempre su 'pronto a guardare'",
    "forceguiprompt-label" : u"Non mostrare ogni volta la finestra di configurazione di Syncplay", # (Inverted)
    "showosd-label" : u"Abilita i messaggi OSD",

    "showosdwarnings-label" : u"Includi gli avvisi (es. file differenti, utenti non pronti)",
    "showsameroomosd-label" : u"Includi gli eventi della tua stanza",
    "shownoncontrollerosd-label" : u"Includi gli eventi dei non gestori nelle stanze gestite",
    "showdifferentroomosd-label" : u"Includi gli eventi di altre stanze",
    "showslowdownosd-label" :u"Includi le notifiche di rallentamento / riavvolgimento",
    "language-label" : u"Lingua:",
    "automatic-language" : u"Predefinita ({})", # Default language
    "showdurationnotification-label" : u"Avvisa in caso di mancata corrispondenza della durata del file",
    "basics-label" : u"Basics",
    "readiness-label" : u"Play/Pause",
    "misc-label" : u"Misc",
    "core-behaviour-title" : u"Core room behaviour",
    "syncplay-internals-title" : u"Syncplay internals",
    "syncplay-mediasearchdirectories-title" : u"Directories to search for media (one path per line)",
    "sync-label" : u"Sync",
    "sync-otherslagging-title" : u"If others are lagging behind...",
    "sync-youlaggging-title" : u"If you are lagging behind...",
    "messages-label" : u"Messages",
    "messages-osd-title" : u"On-screen Display settings",
    "messages-other-title" : u"Other display settings",
    "chat-label" : u"Chat",
    "privacy-label" : u"Privacy", # Currently unused, but will be brought back if more space is needed in Misc tab
    "privacy-title" : u"Privacy settings",
    "unpause-title" : u"If you press play, set as ready and:",
    "unpause-ifalreadyready-option" : u"Unpause if already set as ready",
    "unpause-ifothersready-option" : u"Unpause if already ready or others in room are ready (default)",
    "unpause-ifminusersready-option" : u"Unpause if already ready or if all others ready and min users ready",
    "unpause-always" : u"Always unpause",
    "syncplay-trusteddomains-title": u"Trusted domains (for streaming services and hosted content)",

    "chat-title" : u"Chat message input",
    "chatinputenabled-label" : u"Enable chat input via mpv",
    "chatdirectinput-label" : u"Allow instant chat input (bypass having to press enter key to chat)",
    "chatinputfont-label" : u"Chat input font",
    "chatfont-label" : u"Set font",
    "chatcolour-label" : u"Set colour",
    "chatinputposition-label" : u"Position of message input area in mpv",
    "chat-top-option" : u"Top",
    "chat-middle-option" : u"Middle",
    "chat-bottom-option" : u"Bottom",
    "chatoutputfont-label": u"Chat output font",
    "chatoutputenabled-label": u"Enable chat output in media player (mpv only for now)",
    "chatoutputposition-label": u"Output mode",
    "chat-chatroom-option": u"Chatroom style",
    "chat-scrolling-option": u"Scrolling style",

    "mpv-key-tab-hint": u"[TAB] to toggle access to alphabet row key shortcuts.",
    "mpv-key-hint": u"[ENTER] to send message. [ESC] to escape chat mode.",
    "alphakey-mode-warning-first-line": u"You can temporarily use old mpv bindings with a-z keys.",
    "alphakey-mode-warning-second-line": u"Press [TAB] to return to Syncplay chat mode.",

    "help-label" : u"Help",
    "reset-label" : u"Restore defaults",
    "run-label" : u"Run Syncplay",
    "storeandrun-label" : u"Store configuration and run Syncplay",

    "contact-label" : u"Feel free to e-mail <a href=\"mailto:dev@syncplay.pl\"><nobr>dev@syncplay.pl</nobr></a>, chat via the <a href=\"https://webchat.freenode.net/?channels=#syncplay\"><nobr>#Syncplay IRC channel</nobr></a> on irc.freenode.net, <a href=\"https://github.com/Uriziel/syncplay/issues\"><nobr>raise an issue</nobr></a> via GitHub, <a href=\"https://www.facebook.com/SyncplaySoftware\"><nobr>like us on Facebook</nobr></a>, <a href=\"https://twitter.com/Syncplay/\"><nobr>follow us on Twitter</nobr></a>, or visit <a href=\"http://syncplay.pl/\"><nobr>http://syncplay.pl/</nobr></a>. NOTE: Chat messages are not encrypted so do not use Syncplay to send sensitive information.",

    "joinroom-label" : u"Join room",
    "joinroom-menu-label" : u"Join room {}",
    "seektime-menu-label" : u"Seek to time",
    "undoseek-menu-label" : u"Undo seek",
    "play-menu-label" : u"Play",
    "pause-menu-label" : u"Pause",
    "playbackbuttons-menu-label" : u"Show playback buttons",
    "autoplay-menu-label" : u"Show auto-play button",
    "autoplay-guipushbuttonlabel" : u"Play when all ready",
    "autoplay-minimum-label" : u"Min users:",

    "sendmessage-label" : u"Send",

    "ready-guipushbuttonlabel" : u"I'm ready to watch!",

    "roomuser-heading-label" : u"Room / User",
    "size-heading-label" : u"Size",
    "duration-heading-label" : u"Length",
    "filename-heading-label" : u"Filename",
    "notifications-heading-label" : u"Notifications",
    "userlist-heading-label" : u"List of who is playing what",

    "browseformedia-label" : u"Browse for media files",

    "file-menu-label" : u"&File", # & precedes shortcut key
    "openmedia-menu-label" : u"&Open media file",
    "openstreamurl-menu-label" : u"Open &media stream URL",
    "setmediadirectories-menu-label" : u"Set media &directories",
    "exit-menu-label" : u"E&xit",
    "advanced-menu-label" : u"&Advanced",
    "window-menu-label" : u"&Window",
    "setoffset-menu-label" : u"Set &offset",
    "createcontrolledroom-menu-label" : u"&Create managed room",
    "identifyascontroller-menu-label" : u"&Identify as room operator",
    "settrusteddomains-menu-label" : u"Set &trusted domains",
    "addtrusteddomain-menu-label" : u"Add {} as trusted domain", # Domain

    "playback-menu-label" : u"&Playback",

    "help-menu-label" : u"&Help",
    "userguide-menu-label" : u"Open user &guide",
    "update-menu-label" : u"Check for &update",

    #About dialog
    "about-menu-label": u"&About Syncplay",
    "about-dialog-title": u"About Syncplay",
    "about-dialog-release": u"Version {} release {} on {}",
    "about-dialog-license-text" : u"Licensed under the Apache&nbsp;License,&nbsp;Version 2.0",
    "about-dialog-license-button": u"License",
    "about-dialog-dependencies": u"Dependencies",

    "setoffset-msgbox-label" : u"Set offset",
    "offsetinfo-msgbox-label" : u"Offset (see http://syncplay.pl/guide/ for usage instructions):",

    "promptforstreamurl-msgbox-label" : u"Open media stream URL",
    "promptforstreamurlinfo-msgbox-label" : u"Stream URL",

    "addfolder-label" : u"Add folder",

    "adduris-msgbox-label" : u"Add URLs to playlist (one per line)",
    "editplaylist-msgbox-label" : u"Set playlist (one per line)",
    "trusteddomains-msgbox-label" : u"Domains it is okay to automatically switch to (one per line)",

    "createcontrolledroom-msgbox-label" : u"Create managed room",
    "controlledroominfo-msgbox-label" : u"Enter name of managed room\r\n(see http://syncplay.pl/guide/ for usage instructions):",

    "identifyascontroller-msgbox-label" : u"Identify as room operator",
    "identifyinfo-msgbox-label" : u"Enter operator password for this room\r\n(see http://syncplay.pl/guide/ for usage instructions):",

    "public-server-msgbox-label" : u"Select the public server for this viewing session",

    "megabyte-suffix" : u" MB",

    # Tooltips

    "host-tooltip" : u"Hostname or IP to connect to, optionally including port (e.g. syncplay.pl:8999). Only synchronised with people on same server/port.",
    "name-tooltip" : u"Nickname you will be known by. No registration, so can easily change later. Random name generated if none specified.",
    "password-tooltip" : u"Passwords are only needed for connecting to private servers.",
    "room-tooltip" : u"Room to join upon connection can be almost anything, but you will only be synchronised with people in the same room.",

    "executable-path-tooltip" : u"Location of your chosen supported media player (mpv, VLC, MPC-HC/BE or mplayer2).",
    "media-path-tooltip" : u"Location of video or stream to be opened. Necessary for mplayer2.",
    "player-arguments-tooltip" : u"Additional command line arguments / switches to pass on to this media player.",
    "mediasearcdirectories-arguments-tooltip" : u"Directories where Syncplay will search for media files, e.g. when you are using the click to switch feature. Syncplay will look recursively through sub-folders.",

    "more-tooltip" : u"Display less frequently used settings.",
    "filename-privacy-tooltip" : u"Privacy mode for sending currently playing filename to server.",
    "filesize-privacy-tooltip" : u"Privacy mode for sending size of currently playing file to server.",
    "privacy-sendraw-tooltip" : u"Send this information without obfuscation. This is the default option with most functionality.",
    "privacy-sendhashed-tooltip" : u"Send a hashed version of the information, making it less visible to other clients.",
    "privacy-dontsend-tooltip" : u"Do not send this information to the server. This provides for maximum privacy.",
    "checkforupdatesautomatically-tooltip" : u"Regularly check with the Syncplay website to see whether a new version of Syncplay is available.",
    "slowondesync-tooltip" : u"Reduce playback rate temporarily when needed to bring you back in sync with other viewers. Not supported on MPC-HC/BE.",
    "dontslowdownwithme-tooltip" : u"Means others do not get slowed down or rewinded if your playback is lagging. Useful for room operators.",
    "pauseonleave-tooltip" : u"Pause playback if you get disconnected or someone leaves from your room.",
    "readyatstart-tooltip" : u"Set yourself as 'ready' at start (otherwise you are set as 'not ready' until you change your readiness state)",
    "forceguiprompt-tooltip" : u"Configuration dialogue is not shown when opening a file with Syncplay.", # (Inverted)
    "nostore-tooltip" : u"Run Syncplay with the given configuration, but do not permanently store the changes.", # (Inverted)
    "rewindondesync-tooltip" : u"Jump back when needed to get back in sync. Disabling this option can result in major desyncs!",
    "fastforwardondesync-tooltip" : u"Jump forward when out of sync with room operator (or your pretend position if 'Never slow down or rewind others' enabled).",
    "showosd-tooltip" : u"Sends Syncplay messages to media player OSD.",
    "showosdwarnings-tooltip" : u"Show warnings if playing different file, alone in room, users not ready, etc.",
    "showsameroomosd-tooltip" : u"Show OSD notifications for events relating to room user is in.",
    "shownoncontrollerosd-tooltip" : u"Show OSD notifications for events relating to non-operators who are in managed rooms.",
    "showdifferentroomosd-tooltip" : u"Show OSD notifications for events relating to room user is not in.",
    "showslowdownosd-tooltip" : u"Show notifications of slowing down / reverting on time difference.",
    "showdurationnotification-tooltip" : u"Useful for when a segment in a multi-part file is missing, but can result in false positives.",
    "language-tooltip" : u"Language to be used by Syncplay.",
    "unpause-always-tooltip" : u"If you press unpause it always sets you as ready and unpause, rather than just setting you as ready.",
    "unpause-ifalreadyready-tooltip" : u"If you press unpause when not ready it will set you as ready - press unpause again to unpause.",
    "unpause-ifothersready-tooltip" : u"If you press unpause when not ready, it will only upause if others are ready.",
    "unpause-ifminusersready-tooltip" : u"If you press unpause when not ready, it will only unpause if others are ready and minimum users threshold is met.",
    "trusteddomains-arguments-tooltip" : u"Domains that it is okay for Syncplay to automatically switch to when shared playlists is enabled.",

    "chatinputenabled-tooltip" : u"Enable chat input in mpv (press enter to chat, enter to send, escape to cancel)",
    "chatdirectinput-tooltip" : u"Skip having to press 'enter' to go into chat input mode in mpv. Press TAB in mpv to temporarily disable this feature.",
    "font-label-tooltip" : u"Font used for when entering chat messages in mpv. Client-side only, so doesn't affect what other see.",
    "set-input-font-tooltip" : u"Font family used for when entering chat messages in mpv. Client-side only, so doesn't affect what other see.",
    "set-input-colour-tooltip" : u"Font colour used for when entering chat messages in mpv. Client-side only, so doesn't affect what other see.",
    "chatinputposition-tooltip" : u"Location in mpv where chat input text will appear when you press enter and type.",
    "chatinputposition-top-tooltip" : u"Place chat input at top of mpv window.",
    "chatinputposition-middle-tooltip" : u"Place chat input in dead centre of mpv window.",
    "chatinputposition-bottom-tooltip" : u"Place chat input at bottom of mpv window.",
    "chatoutputenabled-tooltip": u"Show chat messages in OSD (if supported by media player).",
    "font-output-label-tooltip": u"Chat output font.",
    "set-output-font-tooltip": u"Font used for when displaying chat messages.",
    "chatoutputmode-tooltip": u"How chat messages are displayed.",
    "chatoutputmode-chatroom-tooltip": u"Display new lines of chat directly below previous line.",
    "chatoutputmode-scrolling-tooltip": u"Scroll chat text from right to left.",

    "help-tooltip" : u"Opens the Syncplay.pl user guide.",
    "reset-tooltip" : u"Reset all settings to the default configuration.",
    "update-server-list-tooltip" : u"Connect to syncplay.pl to update list of public servers.",

    "joinroom-tooltip" : u"Leave current room and joins specified room.",
    "seektime-msgbox-label" : u"Jump to specified time (in seconds / min:sec). Use +/- for relative seek.",
    "ready-tooltip" : u"Indicates whether you are ready to watch.",
    "autoplay-tooltip" : u"Auto-play when all users who have readiness indicator are ready and minimum user threshold met.",
    "switch-to-file-tooltip" : u"Double click to switch to {}", # Filename
    "sendmessage-tooltip" : u"Send message to room",

    # In-userlist notes (GUI)
    "differentsize-note" : u"Different size!",
    "differentsizeandduration-note" : u"Different size and duration!",
    "differentduration-note" : u"Different duration!",
    "nofile-note" : u"(No file being played)",

    # Server messages to client
    "new-syncplay-available-motd-message" : u"<NOTICE> You are using Syncplay {} but a newer version is available from http://syncplay.pl </NOTICE>",  # ClientVersion

    # Server notifications
    "welcome-server-notification" : u"Welcome to Syncplay server, ver. {0}",  # version
    "client-connected-room-server-notification" : u"{0}({2}) connected to room '{1}'",  # username, host, room
    "client-left-server-notification" : u"{0} left server",  # name
    "no-salt-notification" : u"PLEASE NOTE: To allow room operator passwords generated by this server instance to still work when the server is restarted, please add the following command line argument when running the Syncplay server in the future: --salt {}", #Salt


    # Server arguments
    "server-argument-description" : 'Solution to synchronize playback of multiple MPlayer and MPC-HC/BE instances over the network. Server instance',
    "server-argument-epilog" : 'If no options supplied _config values will be used',
    "server-port-argument" : 'server TCP port',
    "server-password-argument" : 'server password',
    "server-isolate-room-argument" : 'should rooms be isolated?',
    "server-salt-argument" : u"random string used to generate managed room passwords",
    "server-disable-ready-argument" : u"disable readiness feature",
    "server-motd-argument": u"path to file from which motd will be fetched",
    "server-chat-argument" : u"Should chat be disabled?",
    "server-chat-maxchars-argument" : u"Maximum number of characters in a chat message (default is {})", # Default number of characters
    "server-messed-up-motd-unescaped-placeholders": u"Message of the Day has unescaped placeholders. All $ signs should be doubled ($$).",
    "server-messed-up-motd-too-long": u"Message of the Day is too long - maximum of {} chars, {} given.",

    # Server errors
    "unknown-command-server-error" : u"Unknown command {}",  # message
    "not-json-server-error" : u"Not a json encoded string {}",  # message
    "not-known-server-error" : u"You must be known to server before sending this command",
    "client-drop-server-error" : u"Client drop: {} -- {}",  # host, error
    "password-required-server-error" : u"Password required",
    "wrong-password-server-error" : u"Wrong password supplied",
    "hello-server-error" : u"Not enough Hello arguments",

    # Playlists
    "playlist-selection-changed-notification" :  u"{} changed the playlist selection", # Username
    "playlist-contents-changed-notification" : u"{} updated the playlist", # Username
    "cannot-find-file-for-playlist-switch-error" : u"Could not find file {} in media directories for playlist switch!", # Filename
    "cannot-add-duplicate-error" : u"Could not add second entry for '{}' to the playlist as no duplicates are allowed.", #Filename
    "cannot-add-unsafe-path-error" : u"Could not automatically load {} because it is not on a trusted domain. You can switch to the URL manually by double clicking it in the playlist, and add trusted domains via File->Advanced->Set Trusted Domains. If you right click on a URL then you can add its domain as a trusted domain via the context menu.", # Filename
    "sharedplaylistenabled-label" : u"Enable shared playlists",
    "removefromplaylist-menu-label" : u"Remove from playlist",
    "shuffleremainingplaylist-menu-label" : u"Shuffle remaining playlist",
    "shuffleentireplaylist-menuu-label" : u"Shuffle entire playlist",
    "undoplaylist-menu-label" : u"Undo last change to playlist",
    "addfilestoplaylist-menu-label" : u"Add file(s) to bottom of playlist",
    "addurlstoplaylist-menu-label" : u"Add URL(s) to bottom of playlist",
    "editplaylist-menu-label": u"Edit playlist",

    "open-containing-folder": u"Open folder containing this file",
    "addusersfiletoplaylist-menu-label" : u"Add {} file to playlist", # item owner indicator
    "addusersstreamstoplaylist-menu-label" : u"Add {} stream to playlist", # item owner indicator
    "openusersstream-menu-label" : u"Open {} stream", # [username]'s
    "openusersfile-menu-label" : u"Open {} file", # [username]'s
    "item-is-yours-indicator" : u"your", # Goes with addusersfiletoplaylist/addusersstreamstoplaylist
    "item-is-others-indicator" : u"{}'s", # username - goes with addusersfiletoplaylist/addusersstreamstoplaylist

    "playlist-instruction-item-message" : u"Drag file here to add it to the shared playlist.",
    "sharedplaylistenabled-tooltip" : u"Room operators can add files to a synced playlist to make it easy for everyone to watching the same thing. Configure media directories under 'Misc'.",
}
