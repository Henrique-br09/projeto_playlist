import streamlit as st 

generos ={
    'Gospel' : {
        'Isadora pompeu' : 'https://www.youtube.com/watch?v=OEDQj7XucHg&list=RDOEDQj7XucHg&start_radio=1',
        'Brunao morada' : 'https://www.youtube.com/watch?v=ePdRgBWhvog&list=RDePdRgBWhvog&start_radio=1',
        'Casa worship' : 'https://www.youtube.com/watch?v=SFiu3KLNd34&list=RDSFiu3KLNd34&start_radio=1',
        'Fernandinho' : 'https://www.youtube.com/watch?v=u2FOGNSJfX8&list=RDu2FOGNSJfX8&start_radio=1',
    },

    'Sertanejo gospel' : {
        'Daniel & Samuel' : 'https://www.youtube.com/watch?v=SH_YBqPONAE&list=RDSH_YBqPONAE&start_radio=1',               
        'Jonas vilar' : 'https://www.youtube.com/watch?v=MY0iDm0Zw4g&list=RDMY0iDm0Zw4g&start_radio=1',          
        'Elias & Eliseu' : 'https://www.youtube.com/watch?v=RKj8wK9EPOE&list=RDRKj8wK9EPOE&start_radio=1',            
        'Renner Azevedo' : 'https://www.youtube.com/watch?v=AxGv4RG9DqY&list=RDAxGv4RG9DqY&start_radio=1',                        
    }, 

    'Classica' : {
        'Johann Sebatian bach' : 'https://www.youtube.com/watch?v=6JQm5aSjX6g&list=RD6JQm5aSjX6g&start_radio=1',
        'Wolfgang amadeus' : 'https://www.youtube.com/watch?v=Rb0UmrCXxVA&list=RDRb0UmrCXxVA&start_radio=1',
        'Frédéric chopin'  : 'https://www.youtube.com/watch?v=IVpuTD-2SEo&list=RDIVpuTD-2SEo&start_radio=1',       
    },

    'Eletronica' : {
        'Avici' : 'https://www.youtube.com/watch?v=cHHLHGNpCSA&list=RDcHHLHGNpCSA&start_radio=1',
        'Alok' : 'https://www.youtube.com/watch?v=JVpTp8IHdEg&list=RDJVpTp8IHdEg&start_radio=1',
        'David guetta' : 'https://www.youtube.com/watch?v=g7O-7rF0Hqk&list=RDg7O-7rF0Hqk&start_radio=1',
        'Calvin harris' : 'https://www.youtube.com/watch?v=ebXbLfLACGM&list=RDebXbLfLACGM&start_radio=1',
    },
}

st.sidebar.title('Playlist mais tocadas')
st.sidebar.image('imagem.png')

genero = st.sidebar.selectbox('selecione um genero musical:', generos.keys())

artista = st.sidebar.selectbox('selecione um artista:', generos[genero].keys())

st.title(artista)

video, sobre = st.tabs(['video', 'sobre o artista'])

with video:
    st.video(generos[genero][artista])

with sobre:
    if artista == 'Isadora pompeu':
        st.markdown('''
            Isadora Pompeo é uma cantora, compositora e influenciadora digital brasileira,
            nascida em 30 de maio de 1999, em Caxias do Sul, Rio Grande do Sul. Ela é conhecida por sua música cristã contemporânea e lançou seu primeiro álbum
            , "Pra Te Contar os Meus Segredos", em 2017. Desde então, Isadora se tornou um fenômeno na música gospel no Brasil, conquistando uma grande base de fãs nas redes sociais. 
            Além de sua carreira musical, ela é reconhecida por sua presença influente no TikTok e Instagram.
            ''')
        
    elif artista == 'Brunao morada':
        st.markdown('''
            Brunão Morada é um cantor e vocalista da banda Morada, que é uma das maiores bandas gospel do Brasil. A banda foi formada em 2009 em Fernandópolis, 
            São Paulo, e é conhecida por suas canções cristãs que misturam diversos ritmos, incluindo reggae e rock alternativo. Brunão é um dos integrantes principais da banda, 
            que acumulou milhões de visualizações em plataformas de streaming e é frequentemente associado à mensagem de fé e positividade que transmite.
            ''')

    elif artista == 'Casa worship':
        st.markdown('''
            Casa Worship é uma banda brasileira de música cristã contemporânea, formada em 2018 na Igreja Casa Ministério Cristão, em Goiânia. 
            O grupo ganhou notoriedade em 2019 com o lançamento do single "A Casa É Sua", que alcançou mais de 100 milhões de reproduções em plataformas de streaming e mais de 500 milhões de visualizações no YouTube.        
            Em 2023, o álbum "Novo Tempo" foi indicado ao Grammy Latino de Melhor Álbum de Música Cristã em Língua Portuguesa. A banda é conhecida por seu estilo pop rock e forte presença de guitarra elétrica, com destaque para a música de adoração e louvor. 
            ''')
        
    elif artista == 'Fernandinho':
        st.markdown('''
            Fernandinho, cujo nome verdadeiro é Fernando Jerônimo dos Santos Júnior, é um cantor brasileiro de música cristã contemporânea, compositor e pastor evangélico. 
            Ele nasceu em 24 de março de 1973 em Aracaju, Sergipe. Fernandinho é membro da Igreja Mananciais, na Barra da Tijuca, Rio de Janeiro
            ''')
        
    elif artista == 'Daniel & Samuel':
        st.markdown('''
            Daniel e Samuel é uma dupla brasileira de música sertaneja, formada pelos irmãos Daniel José dos Santos e Samuel José dos Santos. Eles têm uma carreira de mais de 30 anos, 
            lançando 28 discos e alcançando milhões de cópias vendidas. A dupla é conhecida por suas músicas que agradam o público evangélico e já venceu o Troféu Talento em 2008 e 2009. 
            Além disso, eles são recordistas do gênero, com mais de 1000 músicas compostas e têm vendido discos de ouro e platina.
            ''')
        
    elif artista == 'Jonas vilar':
            st.markdown('''
            Jonas Vilar é um cantor e pastor brasileiro que iniciou seu ministério aos 19 anos. Ele é conhecido por seu estilo de sertanejo universitário gospel e se destacou em programas de TV nacionais, 
            como "Encontro com Fátima Bernardes" e "Raul Gil". Jonas é o pastor sênior da Igreja Shekinah em São Paulo e é pai de Vitória e Manuela Villar. Ele lançou vários álbuns, incluindo "Você Já Venceu" e "Raízes Sertanejas e Hinos da Harpa".
            ''')

    elif artista == 'Elias & Eliseu':   
        st.markdown('''
           Elias e Eliseu são figuras importantes na Bíblia, especialmente Eliseu, que foi o sucessor de Elias. Elias, cujo nome significa "Meu Deus é salvação",
            foi um profeta que enfrentou desafios espirituais e políticos em Israel. Eliseu, filho de Safate, foi chamado por Deus para servir a Elias e,
            após a ascensão de Elias ao céu, se tornou o principal profeta de Israel, realizando muitos milagres, como a purificação das águas de Jericó e a multiplicação do azeite de uma viúva. 
            A história de Eliseu é registrada principalmente no livro de 2 Reis, onde ele demonstra fé e coragem em seguir o chamado divino.
            ''')    

    elif artista == 'Renner Azevedo':   
            st.markdown('''
            Rick & Renner é uma dupla sertaneja brasileira, formada em 1986 pelos amigos Rick Sollo (vocal) e Renner Reis (vocal). 
            Em mais de 25 anos de carreira, os músicos se apresentaram para um público estimado em 225 milhões de pessoas, com uma média de 15 mil pessoas por show.
            ''')    

    elif artista == 'Johann Sebatian bach':    
            st.markdown(''' 
            Johann Sebastian Bach (21 de março de 1685 - 28 de julho de 1750) foi um compositor, organista e cravista alemão, 
            considerado um dos maiores gênios da música clássica. Ele nasceu em Eisenach, Alemanha, e teve uma formação musical excepcional, 
            aprendendo a tocar cravo e órgão com seu irmão mais velho. Bach é famoso por suas cantatas, como "Jesus, alegria dos homens",
             e por obras como a Missa em Si Menor e os Concertos de Brandenburgo. Sua obra é rica em harmonia e influenciou profundamente a música posterior, 
            sendo considerado um dos maiores compositores da história.
            ''')

    elif artista == 'Wolfgang amadeus': 
            st.markdown('''
            Wolfgang Amadeus Mozart (AFI: ˈvɔlfgaŋ amaˈdeʊs ˈmoːtsaʁtⓘ), batizado Johannes Chrysostomus Wolfgangus Theophilus Mozart,[nota 1] 
            (Salzburgo, 27 de janeiro de 1756 – Viena, 5 de dezembro de 1791) foi um prolífico e influente compositor austríaco do período clássico.
            ''')

    elif artista == 'Frédéric chopin':  
        st.markdown('''
            Frédéric Chopin foi um compositor e pianista polonês da era romântica, nascido em Żelazowa Wola, Polônia, 
            em 1º de março de 1810. Ele é amplamente reconhecido como um dos maiores compositores para piano da história, conhecido por suas prelúdios,
            noturnos, sonatas e baladas. Chopin se destacou por sua técnica refinada e sua capacidade de expressar emoções profundas através da música. 
            Apesar de sua carreira internacional, ele enfrentou problemas de saúde, especialmente tuberculose, que o levaram a morrer em Paris em 17 de outubro de 1849, aos 39 anos. 
            ''')

    elif artista == 'Avici':    
        st.markdown(''' 
            Avicii, cujo nome verdadeiro é Tim Bergling, foi um DJ, produtor musical e cantor sueco, 
            falecido em 20 de abril de 2018. Ele é conhecido por suas músicas eletrônicas icônicas, como "Wake Me Up!",
            "Levels" e "Hey Brother", que redefiniram o gênero EDM. Avicii começou sua carreira musical aos 16 anos e 
            rapidamente se tornou um dos DJs mais populares do mundo, conquistando milhões de fãs com suas melodias cativantes. 
            Apesar de seu sucesso, ele enfrentou problemas de saúde mental e suicidou-se em 2018, deixando um legado duradouro na indústria da música eletrônica. 
            ''')

    elif artista == 'Alok': 
        st.markdown('''
            Alok Achkar Peres Petrillo (Goiânia, 26 de agosto de 1991) é um DJ e produtor musical brasileiro, 
            [5] mais conhecido por seu sucesso mundial de 2016 "Hear Me Now". [6] É atualmente o 4.º melhor DJ do mundo segundo a revista britânica DJ Mag.[7]
            ''')

    elif artista == 'David guetta': 
            st.markdown('''
            David Guetta é um DJ e produtor musical francês, nascido em Paris em 7 de novembro de 1967. 
            Ele é conhecido por suas colaborações com artistas renomados, como Kelly Rowland e Akon, 
            e já vendeu mais de 10 milhões de álbuns e 65 milhões de singles em todo o mundo.
            Guetta alcançou o sucesso global com seu álbum "One Love" (2009), que incluiu hits como "When Love Takes Over" e "Titanium". 
            Ele foi eleito o DJ número um na DJ Mag Top 100 DJs em várias ocasiões e continua a ser uma figura influente na música eletrônica
            ''')

    elif artista == 'Calvin harris':    
        st.markdown('''
            Calvin Harris, nome artístico de Adam Richard Wiles, nasceu em 17 de janeiro de 1984 em Dumfries, Escócia. 
            Ele é um DJ, produtor musical, cantor e compositor renomado, conhecido por seus sucessos nas paradas musicais e por ser um dos DJs mais bem pagos do mundo. 
            Seu primeiro álbum, "I Created Disco", foi lançado em 2007, e desde então, ele se tornou uma figura proeminente na música eletrônica e pop.
            ''')

    

  











