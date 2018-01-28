# coding:utf8

"""Italian dictionary"""

it = {
    "LANGUAGE" : "Italian",

    # Client notifications
    "config-cleared-notification" : "Impostazioni resettate. I cambiamenti saranno memorizzati quando salverai una configurazione valida.",

    "relative-config-notification" : u"Caricato i file di configurazione relativi: {}",

    "connection-attempt-notification" : "Tentativo di connessione a {}:{}",  # Port, IP
    "reconnection-attempt-notification" : "Connessione col server persa, tentativo di riconnesione in corso",
    "disconnection-notification" : "Disconnesso dal server",
    "connection-failed-notification" : "Connessione col server fallita",
    "connected-successful-notification" : "Connessione al server effettuata con successo",
    "retrying-notification" : "%s, Nuovo tentativo in %d secondi...",  # Seconds

    "rewind-notification" : "Riavvolgendo a causa della differenza temporale con {}",  # User
    "fastforward-notification" : "Avanzamento rapido a causa della differenza temporale con {}",  # User
    "slowdown-notification" : "Rallentando a causa della differenza temporale con {}",  # User
    "revert-notification" : "Ritornando alla velocità di riproduzione normale",

    "pause-notification" : u"{} ha messo in pausa",  # User
    "unpause-notification" : u"{} ha ripreso la riproduzione",  # User
    "seek-notification" : u"{} è passato da {} a {}",  # User, from time, to time

    "current-offset-notification" : "Offset corrente: {} secondi",  # Offset

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

    "file-different-notification" : "Il file che stai riproducendo sembra essere diverso da quello di {}",  # User
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
    "notplaying-notification" : "Partecipanti che non stanno riproducendo alcun file:",
    "userlist-room-notification" :  u"Nella stanza '{}':",  # Room
    "userlist-file-notification" : "File",
    "controller-userlist-userflag" : "Gestore",
    "ready-userlist-userflag" : "Pronto",

    "update-check-failed-notification" : u"Controllo automatico degli aggiornamenti di Syncplay {} fallito. Vuoi visitare http://syncplay.pl/ per verificare manualmente la presenza di aggiornamenti?", #Syncplay version
    "syncplay-uptodate-notification" : u"Syncplay è aggiornato",
    "syncplay-updateavailable-notification" : u"Nuova versione di Syncplay disponibile. Vuoi visitare la pagina delle release?",

    "mplayer-file-required-notification" : "Utilizzare Syncplay con mplayer richiede la selezione del file all'avvio",
    "mplayer-file-required-notification/example" : "Esempio di utilizzo: syncplay [opzioni] [url|percorso/]nomefile",
    "mplayer2-required" : "Syncplay non è compatibile con MPlayer 1.x, per favore utilizza mplayer2 or mpv",

    "unrecognized-command-notification" : "Comando non riconosciuto",
    "commandlist-notification" : "Comandi disponibili:",
    "commandlist-notification/room" : "\tr [nome] - cambia stanza",
    "commandlist-notification/list" : "\tl - mostra la lista di utenti",
    "commandlist-notification/undo" : "\tu - annulla l'ultima ricerca",
    "commandlist-notification/pause" : "\tp - attiva o disattiva la pausa",
    "commandlist-notification/seek" : "\t[s][+-]tempo - seek to the given value of time, if + or - is not specified it's absolute time in seconds or min:sec",
    "commandlist-notification/help" : "\th - questo help",
    "commandlist-notification/toggle" : u"\tt - attiva o disattiva lo stato 'Pronto'",
    "commandlist-notification/create" : "\tc [nome] - crea una stanza gestita usando il nome della stanza attuale",
    "commandlist-notification/auth" : "\ta [password] - autentica come gestore della stanza, utilizzando la password del gestore",
    "commandlist-notification/chat" : "\tch [message] - invia un messaggio nella chat della stanza",
    "syncplay-version-notification" : "Versione di Syncplay: {}",  # syncplay.version
    "more-info-notification" : "Maggiori informazioni a: {}",  # projectURL

    "gui-data-cleared-notification" : "Syncplay ha resettato i dati, usati dalla GUI, relativi ai percorsi ed allo stato delle finestre.",
    "language-changed-msgbox-label" : "La lingua sarà cambiata quando avvierai Syncplay.",
    "promptforupdate-label" : u"Ti piacerebbe che, di tanto in tanto, Syncplay controllasse automaticamente la presenza di aggiornamenti?",

    "vlc-interface-version-mismatch": "Stai eseguendo la versione {} del modulo di interfaccia per VLC di Syncplay, ma Syncplay è progettato per essere utilizzato con la versione {} o superiore. Per favore, fai riferimento alla User Guide di Syncplay presso http://syncplay.pl/guide/ per istruzioni su come installare syncplay.lua.",  # VLC interface version, VLC interface min version
    "vlc-interface-oldversion-warning": "Attenzione: Syncplay ha rilevato una vecchia versione del modulo di interfaccia per VLC di Syncplay installata nella cartella di VLC. Per favore, fai riferimento alla User Guide di Syncplay presso http://syncplay.pl/guide/ per istruzioni su come installare syncplay.lua.",
    "media-player-latency-warning": u"Attenzione: il media player ha impiegato {} secondi per rispondere. Se stai avendo problemi di sincronizzazione, chiudi delle applicazioni per liberare le risorse di sistema e, se ciò non dovesse avere alcun effetto, prova un altro media player.", # Seconds to respond
    "vlc-interface-not-installed": "Attenzione: il modulo di interfaccia per VLC di Syncplay non è stato trovato nella cartella di VLC. Se stai utilizzando VLC 2.0, VLC userà il modulo syncplay.lua contenuto nella cartella di Syncplay, ma ciò significa che altri custom script di interfaccia ed estensioni non funzioneranno. Per favore, fai riferimento alla User Guide di Syncplay presso http://syncplay.pl/guide/ per istruzioni su come installare syncplay.lua.",
    "mpv-unresponsive-error": u"mpv non ha risposto per {} secondi, quindi sembra non funzionare correttamente. Per favore, riavvia Syncplay.", # Seconds to respond

    # Client prompts
    "enter-to-exit-prompt" : "Premi Invio per uscire\n",

    # Client errors
    "missing-arguments-error" : "Alcuni argomenti obbligatori non sono stati trovati. Fai riferimento a --help",
    "server-timeout-error" : "Connessione col server scaduta",
    "mpc-slave-error" : "Non è possibile avviare MPC in modalità slave!",
    "mpc-version-insufficient-error" : "Versione di MPC non sufficiente, per favore usa `mpc-hc` >= `{}`",
    "mpc-be-version-insufficient-error" : "Versione di MPC non sufficiente, per favore usa `mpc-be` >= `{}`",
    "mpv-version-error" : "Syncplay non è compatibile con questa versione di mpv. Per favore usa un'altra versione di mpv (es. Git HEAD).",
    "player-file-open-error" : "Il player non è riuscito ad aprire il file",
    "player-path-error" : "Il path del player non è configurato correttamente. I player supportati sono: mpv, VLC, MPC-HC, MPC-BE e mplayer2",
    "hostname-empty-error" : "Hostname non può essere vuoto",
    "empty-error" : "{} non può esssere vuoto",  # Configuration
    "media-player-error": "Errore media player: \"{}\"",  # Error line
    "unable-import-gui-error": "Non è possibile importare le librerie GUI. Hai bisogno di PySide per poter utilizzare la GUI.",

    "arguments-missing-error" : "Alcuni argomenti obbligatori non sono stati trovati. Fai riferimento a --help",

    "unable-to-start-client-error" : "Impossibile avviare il client",

    "player-path-config-error": "Il path del player non è configurato correttamente. I player supportati sono: mpv, VLC, MPC-HC, MPC-BE e mplayer2.",
    "no-file-path-config-error" :"Un file deve essere selezionato prima di avviare il player",
    "no-hostname-config-error": "Hostname non può essere vuoto",
    "invalid-port-config-error" : "La porta deve essere valida",
    "empty-value-config-error" : "{} non può essere vuoto", # Config option

    "not-json-error" : "Non è una stringa con codifica JSON\n",
    "hello-arguments-error" : "Argomenti Hello non sufficienti\n",
    "version-mismatch-error" : "La versione del client è diversa da quella del server\n",
    "vlc-failed-connection": "Impossibile collegarsi a VLC. Se non hai installato syncplay.lua e stai usando l'ultima versione di VLC, fai riferimento a http://syncplay.pl/LUA/ per istruzioni.",
    "vlc-failed-noscript": "VLC ha segnalato che lo script di interfaccia syncplay.lua non è stato installato. Per favore, fai riferimento a http://syncplay.pl/LUA/ per istruzioni.",
    "vlc-failed-versioncheck": "Questa versione di VLC non è supportata da Syncplay.",

    "feature-sharedPlaylists" : u"shared playlists", # used for not-supported-by-server-error
    "feature-chat" : u"chat", # used for not-supported-by-server-error
    "feature-readiness" : u"readiness", # used for not-supported-by-server-error
    "feature-managedRooms" : u"managed rooms", # used for not-supported-by-server-error

    "not-supported-by-server-error" : u"The {} feature is not supported by this server..", #feature
    "shared-playlists-not-supported-by-server-error" : "The shared playlists feature may not be supported by the server. To ensure that it works correctly requires a server running Syncplay  {}+, but the server is running Syncplay {}.", #minVersion, serverVersion
    "shared-playlists-disabled-by-server-error" : "The shared playlist feature has been disabled in the server configuration. To use this feature you will need to connect to a different server.",

    "invalid-seek-value" : u"Invalid seek value",
    "invalid-offset-value" : u"Invalid offset value",

    "switch-file-not-found-error" : u"Could not switch to file '{0}'. Syncplay looks in specified media directories.", # File not found
    "folder-search-timeout-error" : u"The search for media in media directories was aborted as it took too long to search through '{}'. This will occur if you select a folder with too many sub-folders in your list of media folders to search through. For automatic file switching to work again please select File->Set Media Directories in the menu bar and remove this directory or replace it with an appropriate sub-folder. If the folder is actually fine then you can re-enable it by selecting File->Set Media Directories and pressing 'OK'.", #Folder
    "folder-search-first-file-timeout-error" : u"The search for media in '{}' was aborted as it took too long to access the directory. This could happen if it is a network drive or if you configure your drive to spin down after a period of inactivity. For automatic file switching to work again please go to File->Set Media Directories and either remove the directory or resolve the issue (e.g. by changing power saving settings).", #Folder
    "added-file-not-in-media-directory-error" : u"You loaded a file in '{}' which is not a known media directory. You can add this as a media directory by selecting File->Set Media Directories in the menu bar.", #Folder
    "no-media-directories-error" : u"No media directories have been set. For shared playlist and file switching features to work properly please select File->Set Media Directories and specify where Syncplay should look to find media files.",
    "cannot-find-directory-error" : u"Could not find media directory '{}'. To update your list of media directories please select File->Set Media Directories from the menu bar and specify where Syncplay should look to find media files.",

    "failed-to-load-server-list-error" : u"Failed to load public server list. Please visit http://www.syncplay.pl/ in your browser.",

    # Client arguments
    "argument-description" : 'Solution to synchronize playback of multiple media player instances over the network.',
    "argument-epilog" : 'If no options supplied _config values will be used',
    "nogui-argument" : 'show no GUI',
    "host-argument" : 'server\'s address',
    "name-argument" : 'desired username',
    "debug-argument" : 'debug mode',
    "force-gui-prompt-argument" : 'make configuration prompt appear',
    "no-store-argument" : 'don\'t store values in .syncplay',
    "room-argument" : 'default room',
    "password-argument" : 'server password',
    "player-path-argument" : 'path to your player executable',
    "file-argument" : 'file to play',
    "args-argument" : 'player options, if you need to pass options starting with - prepend them with single \'--\' argument',
    "clear-gui-data-argument" : 'resets path and window state GUI data stored as QSettings',
    "language-argument" :'language for Syncplay messages (de/en/ru)',

    "version-argument" : 'prints your version',
    "version-message" : "You're using Syncplay version {} ({})",

    # Client labels
    "config-window-title" : "Syncplay configuration",

    "connection-group-title" : "Connection settings",
    "host-label" : "Server address: ",
    "name-label" :  "Username (optional):",
    "password-label" :  "Server password (if any):",
    "room-label" : "Default room: ",

    "media-setting-title" : "Media player settings",
    "executable-path-label" : "Path to media player:",
    "media-path-label" : "Path to video (optional):",
    "player-arguments-label" : "Player arguments (if any):",
    "browse-label" : "Browse",
    "update-server-list-label" : u"Update list",

    "more-title" : "Show more settings",
    "never-rewind-value" : "Never",
    "seconds-suffix" : " secs",
    "privacy-sendraw-option" : "Send raw",
    "privacy-sendhashed-option" : "Send hashed",
    "privacy-dontsend-option" : "Don't send",
    "filename-privacy-label" : "Filename information:",
    "filesize-privacy-label" : "File size information:",
    "checkforupdatesautomatically-label" : "Check for Syncplay updates automatically",
    "slowondesync-label" : "Slow down on minor desync (not supported on MPC-HC/BE)",
    "rewindondesync-label" : "Rewind on major desync (recommended)",
    "fastforwardondesync-label" : "Fast-forward if lagging behind (recommended)",
    "dontslowdownwithme-label" : "Never slow down or rewind others (experimental)",
    "pausing-title" : u"Pausing",
    "pauseonleave-label" : "Pause when user leaves (e.g. if they are disconnected)",
    "readiness-title" : u"Initial readiness state",
    "readyatstart-label" : "Set me as 'ready to watch' by default",
    "forceguiprompt-label" : "Don't always show the Syncplay configuration window", # (Inverted)
    "showosd-label" : "Enable OSD Messages",

    "showosdwarnings-label" : "Include warnings (e.g. when files are different, users not ready)",
    "showsameroomosd-label" : "Include events in your room",
    "shownoncontrollerosd-label" : "Include events from non-operators in managed rooms",
    "showdifferentroomosd-label" : "Include events in other rooms",
    "showslowdownosd-label" :"Include slowing down / reverting notifications",
    "language-label" : "Language:",
    "automatic-language" : u"Default ({})", # Default language
    "showdurationnotification-label" : "Warn about media duration mismatches",
    "basics-label" : "Basics",
    "readiness-label" : u"Play/Pause",
    "misc-label" : u"Misc",
    "core-behaviour-title" : "Core room behaviour",
    "syncplay-internals-title" : u"Syncplay internals",
    "syncplay-mediasearchdirectories-title" : u"Directories to search for media (one path per line)",
    "sync-label" : "Sync",
    "sync-otherslagging-title" : "If others are lagging behind...",
    "sync-youlaggging-title" : "If you are lagging behind...",
    "messages-label" : "Messages",
    "messages-osd-title" : "On-screen Display settings",
    "messages-other-title" : "Other display settings",
    "chat-label" : u"Chat",
    "privacy-label" : "Privacy", # Currently unused, but will be brought back if more space is needed in Misc tab
    "privacy-title" : "Privacy settings",
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

    "help-label" : "Help",
    "reset-label" : "Restore defaults",
    "run-label" : "Run Syncplay",
    "storeandrun-label" : "Store configuration and run Syncplay",

    "contact-label" : "Feel free to e-mail <a href=\"mailto:dev@syncplay.pl\"><nobr>dev@syncplay.pl</nobr></a>, chat via the <a href=\"https://webchat.freenode.net/?channels=#syncplay\"><nobr>#Syncplay IRC channel</nobr></a> on irc.freenode.net, <a href=\"https://github.com/Uriziel/syncplay/issues\"><nobr>raise an issue</nobr></a> via GitHub, <a href=\"https://www.facebook.com/SyncplaySoftware\"><nobr>like us on Facebook</nobr></a>, <a href=\"https://twitter.com/Syncplay/\"><nobr>follow us on Twitter</nobr></a>, or visit <a href=\"http://syncplay.pl/\"><nobr>http://syncplay.pl/</nobr></a>. NOTE: Chat messages are not encrypted so do not use Syncplay to send sensitive information.",

    "joinroom-label" : "Join room",
    "joinroom-menu-label" : u"Join room {}",
    "seektime-menu-label" : "Seek to time",
    "undoseek-menu-label" : "Undo seek",
    "play-menu-label" : "Play",
    "pause-menu-label" : "Pause",
    "playbackbuttons-menu-label" : u"Show playback buttons",
    "autoplay-menu-label" : u"Show auto-play button",
    "autoplay-guipushbuttonlabel" : u"Play when all ready",
    "autoplay-minimum-label" : u"Min users:",

    "sendmessage-label" : u"Send",

    "ready-guipushbuttonlabel" : u"I'm ready to watch!",

    "roomuser-heading-label" : "Room / User",
    "size-heading-label" : "Size",
    "duration-heading-label" : "Length",
    "filename-heading-label" : "Filename",
    "notifications-heading-label" : "Notifications",
    "userlist-heading-label" : "List of who is playing what",

    "browseformedia-label" : "Browse for media files",

    "file-menu-label" : "&File", # & precedes shortcut key
    "openmedia-menu-label" : "&Open media file",
    "openstreamurl-menu-label" : "Open &media stream URL",
    "setmediadirectories-menu-label" : u"Set media &directories",
    "exit-menu-label" : "E&xit",
    "advanced-menu-label" : "&Advanced",
    "window-menu-label" : "&Window",
    "setoffset-menu-label" : "Set &offset",
    "createcontrolledroom-menu-label" : "&Create managed room",
    "identifyascontroller-menu-label" : "&Identify as room operator",
    "settrusteddomains-menu-label" : u"Set &trusted domains",
    "addtrusteddomain-menu-label" : u"Add {} as trusted domain", # Domain

    "playback-menu-label" : u"&Playback",

    "help-menu-label" : "&Help",
    "userguide-menu-label" : "Open user &guide",
    "update-menu-label" : "Check for &update",

    #About dialog
    "about-menu-label": u"&About Syncplay",
    "about-dialog-title": u"About Syncplay",
    "about-dialog-release": u"Version {} release {} on {}",
    "about-dialog-license-text" : u"Licensed under the Apache&nbsp;License,&nbsp;Version 2.0",
    "about-dialog-license-button": u"License",
    "about-dialog-dependencies": u"Dependencies",

    "setoffset-msgbox-label" : "Set offset",
    "offsetinfo-msgbox-label" : "Offset (see http://syncplay.pl/guide/ for usage instructions):",

    "promptforstreamurl-msgbox-label" : "Open media stream URL",
    "promptforstreamurlinfo-msgbox-label" : "Stream URL",

    "addfolder-label" : u"Add folder",

    "adduris-msgbox-label" : u"Add URLs to playlist (one per line)",
    "editplaylist-msgbox-label" : u"Set playlist (one per line)",
    "trusteddomains-msgbox-label" : u"Domains it is okay to automatically switch to (one per line)",

    "createcontrolledroom-msgbox-label" : "Create managed room",
    "controlledroominfo-msgbox-label" : "Enter name of managed room\r\n(see http://syncplay.pl/guide/ for usage instructions):",

    "identifyascontroller-msgbox-label" : "Identify as room operator",
    "identifyinfo-msgbox-label" : "Enter operator password for this room\r\n(see http://syncplay.pl/guide/ for usage instructions):",

    "public-server-msgbox-label" : u"Select the public server for this viewing session",

    "megabyte-suffix" : " MB",

    # Tooltips

    "host-tooltip" : "Hostname or IP to connect to, optionally including port (e.g. syncplay.pl:8999). Only synchronised with people on same server/port.",
    "name-tooltip" : "Nickname you will be known by. No registration, so can easily change later. Random name generated if none specified.",
    "password-tooltip" : "Passwords are only needed for connecting to private servers.",
    "room-tooltip" : "Room to join upon connection can be almost anything, but you will only be synchronised with people in the same room.",

    "executable-path-tooltip" : "Location of your chosen supported media player (mpv, VLC, MPC-HC/BE or mplayer2).",
    "media-path-tooltip" : "Location of video or stream to be opened. Necessary for mplayer2.",
    "player-arguments-tooltip" : "Additional command line arguments / switches to pass on to this media player.",
    "mediasearcdirectories-arguments-tooltip" : u"Directories where Syncplay will search for media files, e.g. when you are using the click to switch feature. Syncplay will look recursively through sub-folders.",

    "more-tooltip" : "Display less frequently used settings.",
    "filename-privacy-tooltip" : "Privacy mode for sending currently playing filename to server.",
    "filesize-privacy-tooltip" : "Privacy mode for sending size of currently playing file to server.",
    "privacy-sendraw-tooltip" : "Send this information without obfuscation. This is the default option with most functionality.",
    "privacy-sendhashed-tooltip" : "Send a hashed version of the information, making it less visible to other clients.",
    "privacy-dontsend-tooltip" : "Do not send this information to the server. This provides for maximum privacy.",
    "checkforupdatesautomatically-tooltip" : "Regularly check with the Syncplay website to see whether a new version of Syncplay is available.",
    "slowondesync-tooltip" : "Reduce playback rate temporarily when needed to bring you back in sync with other viewers. Not supported on MPC-HC/BE.",
    "dontslowdownwithme-tooltip" : "Means others do not get slowed down or rewinded if your playback is lagging. Useful for room operators.",
    "pauseonleave-tooltip" : "Pause playback if you get disconnected or someone leaves from your room.",
    "readyatstart-tooltip" : "Set yourself as 'ready' at start (otherwise you are set as 'not ready' until you change your readiness state)",
    "forceguiprompt-tooltip" : "Configuration dialogue is not shown when opening a file with Syncplay.", # (Inverted)
    "nostore-tooltip" : "Run Syncplay with the given configuration, but do not permanently store the changes.", # (Inverted)
    "rewindondesync-tooltip" : "Jump back when needed to get back in sync. Disabling this option can result in major desyncs!",
    "fastforwardondesync-tooltip" : "Jump forward when out of sync with room operator (or your pretend position if 'Never slow down or rewind others' enabled).",
    "showosd-tooltip" : "Sends Syncplay messages to media player OSD.",
    "showosdwarnings-tooltip" : "Show warnings if playing different file, alone in room, users not ready, etc.",
    "showsameroomosd-tooltip" : "Show OSD notifications for events relating to room user is in.",
    "shownoncontrollerosd-tooltip" : "Show OSD notifications for events relating to non-operators who are in managed rooms.",
    "showdifferentroomosd-tooltip" : "Show OSD notifications for events relating to room user is not in.",
    "showslowdownosd-tooltip" : "Show notifications of slowing down / reverting on time difference.",
    "showdurationnotification-tooltip" : "Useful for when a segment in a multi-part file is missing, but can result in false positives.",
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

    "help-tooltip" : "Opens the Syncplay.pl user guide.",
    "reset-tooltip" : "Reset all settings to the default configuration.",
    "update-server-list-tooltip" : u"Connect to syncplay.pl to update list of public servers.",

    "joinroom-tooltip" : "Leave current room and joins specified room.",
    "seektime-msgbox-label" : "Jump to specified time (in seconds / min:sec). Use +/- for relative seek.",
    "ready-tooltip" : "Indicates whether you are ready to watch.",
    "autoplay-tooltip" : "Auto-play when all users who have readiness indicator are ready and minimum user threshold met.",
    "switch-to-file-tooltip" : u"Double click to switch to {}", # Filename
    "sendmessage-tooltip" : u"Send message to room",

    # In-userlist notes (GUI)
    "differentsize-note" : "Different size!",
    "differentsizeandduration-note" : "Different size and duration!",
    "differentduration-note" : "Different duration!",
    "nofile-note" : "(No file being played)",

    # Server messages to client
    "new-syncplay-available-motd-message" : "<NOTICE> You are using Syncplay {} but a newer version is available from http://syncplay.pl </NOTICE>",  # ClientVersion

    # Server notifications
    "welcome-server-notification" : "Welcome to Syncplay server, ver. {0}",  # version
    "client-connected-room-server-notification" : u"{0}({2}) connected to room '{1}'",  # username, host, room
    "client-left-server-notification" : u"{0} left server",  # name
    "no-salt-notification" : "PLEASE NOTE: To allow room operator passwords generated by this server instance to still work when the server is restarted, please add the following command line argument when running the Syncplay server in the future: --salt {}", #Salt


    # Server arguments
    "server-argument-description" : 'Solution to synchronize playback of multiple MPlayer and MPC-HC/BE instances over the network. Server instance',
    "server-argument-epilog" : 'If no options supplied _config values will be used',
    "server-port-argument" : 'server TCP port',
    "server-password-argument" : 'server password',
    "server-isolate-room-argument" : 'should rooms be isolated?',
    "server-salt-argument" : "random string used to generate managed room passwords",
    "server-disable-ready-argument" : u"disable readiness feature",
    "server-motd-argument": "path to file from which motd will be fetched",
    "server-chat-argument" : "Should chat be disabled?",
    "server-chat-maxchars-argument" : u"Maximum number of characters in a chat message (default is {})", # Default number of characters
    "server-messed-up-motd-unescaped-placeholders": "Message of the Day has unescaped placeholders. All $ signs should be doubled ($$).",
    "server-messed-up-motd-too-long": u"Message of the Day is too long - maximum of {} chars, {} given.",

    # Server errors
    "unknown-command-server-error" : u"Unknown command {}",  # message
    "not-json-server-error" : "Not a json encoded string {}",  # message
    "not-known-server-error" : "You must be known to server before sending this command",
    "client-drop-server-error" : u"Client drop: {} -- {}",  # host, error
    "password-required-server-error" : "Password required",
    "wrong-password-server-error" : "Wrong password supplied",
    "hello-server-error" : "Not enough Hello arguments",

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
