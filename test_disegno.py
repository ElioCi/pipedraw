import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
#from urllib.parse import urlparse
#from http.cookies import SimpleCookie
import requests

# Funzione per impostare un cookie
#def set_cookie(key, value):
#    js = f"""
#    <script>
#    document.cookie = "{key}={value}; path=/";
#    </script>
#    """
#    st.markdown(js, unsafe_allow_html=True)

# Funzione per ottenere un cookie
#def get_cookie(key):
#    cookies = SimpleCookie(st.experimental_get_query_params().get('_cookies', [""])[0])
#    return cookies.get(key).value if key in cookies else None

## Verifica se il parametro 'auth' è presente nella query string
#query_params = st.experimental_get_query_params()
#if "auth" in query_params and query_params["auth"][0] == "true":
#    # Imposta un cookie per identificare che l'utente è autorizzato
#    set_cookie("authorized", "true")
#elif get_cookie("authorized") != "true":
#    # Se il cookie non è presente, reindirizza al sito WordPress
#    st.markdown("""<script>window.location.href = 'https://enginapps.it';</script>""", unsafe_allow_html=True)
#    st.stop()

# Il resto del codice della tua app Streamlit
#st.title('Benvenuto nella mia App Streamlit!')
#st.write('Questa è la tua app, accessibile solo tramite il sito WordPress.')

# Funzione per validare il token
def validate_token(token):
    api_url = f"https://enginapps.it/wp-json/myplugin/v1/validate_token?token={token}"
    response = requests.get(api_url)
    
    # Verifica lo stato della risposta
    if response.status_code == 200:
        return True
    return False

# Estrai il token dai parametri della query
query_params = st.experimental_get_query_params()
token = query_params.get("token", [None])[0]

# Verifica se il token è presente e valido
if token and validate_token(token):
    st.title('Benvenuto nella mia App Streamlit!')
    st.write('Questa è la tua app, accessibile solo tramite il sito WordPress.')
else:
    st.markdown("""<script>window.location.href = 'https://tuosito.com';</script>""", unsafe_allow_html=True)
    st.stop()

# Titolo dell'applicazione
st.title("Sezione di un Tubo con Doppio Isolamento e Lamierino Esterno")

# Parametri del tubo e degli strati
tubo_radius1 = 0.48
tubo_thk = 0.02


first_insulation_thickness = 0.1
second_insulation_thickness = 0.1
lamierino_thickness = 0.02
axis_length = 2  # Lunghezza degli assi centrali
tubo_radius = tubo_radius1+tubo_thk
# Creazione della figura e dell'asse
fig, ax = plt.subplots(figsize=(8, 8))  # Dimensione della figura

# Disegna il lamierino esterno
lamierino = patches.Circle((0, 0), tubo_radius + first_insulation_thickness + second_insulation_thickness + lamierino_thickness, 
                           edgecolor='black', facecolor='lightgray', label='Lamierino Esterno')

# Disegna il secondo strato di isolamento
second_insulation = patches.Circle((0, 0), tubo_radius + first_insulation_thickness + second_insulation_thickness, 
                                   edgecolor='black', facecolor='lightgreen', label='Secondo Strato di Isolamento')

# Disegna il primo strato di isolamento
first_insulation = patches.Circle((0, 0), tubo_radius + first_insulation_thickness, 
                                  edgecolor='black', facecolor='lightblue', label='Primo Strato di Isolamento')
#ax.text(0, tubo_radius + first_insulation_thickness,'Primo Strato di Isolamento', ha='center', va='bottom', fontsize=7)

# Disegna il tubo centrale
lbl1 = "Sect_1"
tubo = patches.Circle((0, 0), tubo_radius1, edgecolor='black', facecolor='white', label='')
tubo1 = patches.Circle((0, 0), tubo_radius1+tubo_thk, edgecolor='black', facecolor='red', label= "Pipe")


# Etichetta per il tubo centrale

lbl1 = "Sect_1"
ax.text(0, tubo_radius/4,
        lbl1, ha='center', va='top', fontsize=7)

# Aggiungi i cerchi all'asse
ax.add_patch(lamierino)
ax.add_patch(second_insulation)
ax.add_patch(first_insulation)
ax.add_patch(tubo1)
ax.add_patch(tubo)


# Disegna gli assi centrali trattati
#ax.axhline(0, color='black', linestyle='--', linewidth=1, label='Asse Orizzontale')
#ax.axvline(0, color='black', linestyle=':', linewidth=1, label='Asse Verticale')

# Disegna gli assi centrali con stili uniformi e corti
# Asse verticale
ax.plot([0, 0], [-axis_length / 2, axis_length / 2], color='#3282F6', linestyle='dashdot', linewidth=1, label='')
# Asse orizzontale
ax.plot([-axis_length / 2, axis_length / 2], [0, 0], color='#3282F6', linestyle='dashdot', linewidth=1, label='')

# Imposta l'asse per avere proporzioni uguali e rimuovi assi
ax.set_aspect('equal')
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.axis('off')  # Nascondi gli assi

# Aggiungi legenda con dimensioni ridotte
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right', fontsize='small', frameon=False)  # Legend con testo piccolo

# Salva il grafico come immagine
image_path = 'files/tubo_isolamento.png'
plt.savefig(image_path, bbox_inches='tight')
plt.close()

# Mostra il grafico in Streamlit
st.pyplot(fig)
