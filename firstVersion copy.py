import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk
import datetime as dt
import plotly.express as px
import ipywidgets as widgets
from plotly.subplots import make_subplots
import plotly.graph_objects as go

acteur_par_periode = pd.read_csv("https://raw.githubusercontent.com/BerengerQueune/ABC-Data/main/Berenger/Streamlit/acteur_par_periode.csv?token=AU6BUZWYJ6GYLJLQVDQCLZTBSZ2NK")
link = 'https://raw.githubusercontent.com/BerengerQueune/ABC-Data/main/Berenger/Streamlit/top10.csv?token=AU6BUZSEQED65VJVLNSX4FLBS2IYO'
top10 = pd.read_csv(link)
presence_acteur = pd.read_csv('https://raw.githubusercontent.com/BerengerQueune/ABC-Data/main/Berenger/Streamlit/presence_acteurs.csv?token=AU6BUZRUOZP7577TQEBP5ODBS2IXQ')
link2 = 'https://raw.githubusercontent.com/BerengerQueune/ABC-Data/main/Berenger/Streamlit/film3.csv?token=AU6BUZQSZO7FES64E636CRLBS2IWM'
film = pd.read_csv(link2)
link3 = 'https://raw.githubusercontent.com/BerengerQueune/ABC-Data/main/Berenger/Streamlit/concat_liste50.csv?token=AU6BUZSY6OPPE25EYFUWFELBS2IS4'
link4 = 'https://raw.githubusercontent.com/BerengerQueune/ABC-Data/main/Berenger/Streamlit/concat_listeTopFilm.csv?token=AU6BUZUX7HJJXUSIP47YANLBS2IVA'
link5 = 'https://raw.githubusercontent.com/BerengerQueune/ABC-Data/main/Berenger/Streamlit/concat_listeTopTV.csv?token=AU6BUZWRESNKYQ36Y652SJLBS2IVW'
concat_liste_50 = pd.read_csv(link3)
concat_listeTopFilm = pd.read_csv(link4)
concat_listeTopTV = pd.read_csv(link5)


#st.set_page_config( layout='wide')


def main():

    st.title("TEST")
    menu = ["Home", "Search", "About"]

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == 'Home':
        st.subheader("Home")

        with st.expander("Title"):
            mytext = st.text_area("Type Here")
            st.write(mytext)
            st.success("Hello")

    elif choice == "Search":
        st.subheader("Search By Year")


    else:
        st.subheader("About")

main()


st.title("Projet : recommandations de films")  # add a title

st.write("Ce projet effectu?? au sein de l'??cole Wild Code School a pour but de nous faire cr??er un moteur de recommandations de films.")

st.write("Un cin??ma en perte de vitesse situ?? dans la Creuse vous contacte. Il a d??cid?? de passer le cap du digital en cr??ant un site Internet taill?? pour les locaux.")

st.write("Pour commencer, nous devons explorer la base de donn??es afin de r??pondre aux questions suivantes :")
st.write("- Quels sont les pays qui produisent le plus de films ?")
st.write("- Quels sont les acteurs les plus pr??sents ? ?? quelle p??riode ?")
st.write("- La dur??e moyenne des films s???allonge ou se raccourcit avec les ann??es ?")
st.write("- Les acteurs de s??rie sont-ils les m??mes qu???au cin??ma ?")
st.write("- Les acteurs ont en moyenne quel ??ge ?")
st.write("- Quels sont les films les mieux not??s ? Partagent-ils des caract??ristiques communes ?")


fig = px.bar(presence_acteur, x="primaryName", y ='index', color = 'index',
    title = 'Quels sont les acteurs les plus pr??sents ?',
    labels = {'primaryName': 'Nombre de films', 'index': 'Acteurs'},
    width=800, height=600)

fig.update_layout(showlegend=False, title_x=0.5, yaxis={'visible': True}, template='plotly_dark')

st.plotly_chart(fig)

fig = px.bar(acteur_par_periode, x = 'count', y="rank", text ='primaryName', color = 'primaryName',
    title = 'Quels sont les acteurs les plus pr??sents par p??riodes ?',
    labels = {'startYear': 'P??riode', 'primaryName': 'Acteurs'},
    orientation='h',
    animation_frame="startYear",
    range_x=[0,150],
    range_y=[0,6],
    width=800, height=500)
 
fig.update_traces(textfont_size=12, textposition='outside')
fig.update_layout(template='plotly_dark')
fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 1000

fig.update_layout(showlegend=False, title_x=0.5)

st.plotly_chart(fig)

test5 = px.bar(top10, x='Pays', y='Nb de films', color="Nb de films", color_continuous_scale=px.colors.sequential.Viridis, title = 'Pays produisants le plus de film depuis 1960', width=700, height=500, template='plotly_dark')

st.plotly_chart(test5)



######################
fig = make_subplots(rows=2, cols=2)

fig.add_trace(go.Line(x = film["startYear"], y=film["runtimeMinutes"]),
              row=1, col=1)

fig.add_trace(go.Line(x = film["startYear"], y=film["runtimeMinutes"]),
              row=1, col=2)

fig.add_trace(go.Line(x = film["startYear"], y=film["runtimeMinutes"]),
              row=2, col=1)

fig.add_trace(go.Line(x = film["startYear"], y=film["runtimeMinutes"]),
              row=2, col=2)

fig.update_xaxes(title_text="", row=1, col=1)
fig.update_yaxes(title_text="", row=1, col=1)

fig.update_xaxes(title_text="", row=1, col=2)
fig.update_yaxes(title_text="", row=1, col=2, range=[80, 100])

fig.update_xaxes(title_text="", row=1, col=1)
fig.update_yaxes(title_text="", row=2, col=1, range=[50, 100])

fig.update_xaxes(title_text="", row=1, col=2)
fig.update_yaxes(title_text="", row=2, col=2, range=[0, 100])

fig.update_layout(height=1000, width=1400, title_text="Evolution de la dur??e des films en minutes depuis 1960", title_x=0.5, showlegend=False, template='plotly_dark', autosize=False)

st.plotly_chart(fig)
######################



fig = px.bar(data_frame = concat_liste_50, x= "primaryName", y="nb", color = 'type', color_discrete_sequence=["darkred", "green"],labels=dict(primaryName="Nom de l'acteur", nb="Nombre de films"))
fig.update_layout(title_text="Top 20 des acteurs ayant tourn??s autant au cin??ma qu'?? la TV", width=1000, height=600, template='plotly_dark')

st.plotly_chart(fig)



fig = px.bar(data_frame = concat_listeTopFilm, x= "primaryName", y="nb", color = 'type', color_discrete_sequence=["blue", "lime"], labels=dict(primaryName="Nom de l'acteur", nb="Nombre de films", color = 'type'))
fig.update_layout(title_text="Top 20 des acteurs ayant tourn??s le plus du film au cin??ma", title_x=0.5, width=1000, height=600, template='plotly_dark')

st.plotly_chart(fig)


fig = px.bar(data_frame = concat_listeTopTV, x= "primaryName", y="nb", color = 'type', color_discrete_sequence=["orange", "olive"], labels=dict(primaryName="Nom de l'acteur", nb="Nombre de films"))
fig.update_layout(title_text="Top 20 des acteurs ayant tourn??s le plus du film ?? la t??l??vision", title_x=0.5, width=1000, height=600, template='plotly_dark')

st.plotly_chart(fig)