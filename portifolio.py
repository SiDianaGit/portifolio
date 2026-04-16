import streamlit as st
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

img_base64 = get_base64_image("simone.png")

# -----------------------------------------------------------------------------
# Configuração da Página e Qualidade Não Funcional (SEO/Responsividade)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Engenharia de Dados & IA | Portfólio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS para aplicar o Dark Mode minimalista (Estilo Linear) e o formato Bento Grid
st.markdown("""
<style>
    /* Dark Theme & Minimalist Typography */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #0E0E10;
        color: #F4F4F5;
    }
    
    /* Hero Section */
    .hero-title {
        font-size: 3.8rem;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #FFF, #71717A);
        -webkit-background-clip: text;
        -webkit-text-fill-color: solid;
        line-height: 1.1;
        margin-bottom: 16px;
    }
    .hero-subtitle {
        font-size: 1.3rem;
        color: #A1A1AA;
        margin-bottom: 30px;
        line-height: 1.5;
    }
    
    /* Bento Grid Cards */
    .bento-card {
        background-color: #18181B;
        border: 1px solid #27272A;
        border-radius: 16px;
        padding: 24px;
        height: 100%;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .bento-card:hover {
        transform: translateY(-4px);
        border-color: #52525B;
    }
    .tag {
        background-color: #27272A;
        color: #D4D4D8;
        padding: 4px 12px;
        border-radius: 99px;
        font-size: 0.8rem;
        margin-right: 8px;
        display: inline-block;
        margin-bottom: 8px;
        font-weight: 600;
    }
    
    /* Timeline */
    .timeline-item {
        border-left: 2px solid #27272A;
        padding-left: 24px;
        margin-bottom: 32px;
        position: relative;
    }
    .timeline-item::before {
        content: '';
        position: absolute;
        width: 14px;
        height: 14px;
        background-color: #0E0E10;
        border: 2px solid #F4F4F5;
        border-radius: 50%;
        left: -8px;
        top: 6px;
    }
    /* Estilização da Foto de Perfil */
    .profile-pic-container {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .profile-pic {
        border-radius: 50%;
        border: 3px solid #FF4B4B;
        width: 180px;
        height: 180px;
        object-fit: cover;
        margin-bottom: 20px;
    }
    /* Ajustes para telas pequenas (Celulares) */
    @media (max-width: 768px) {
        .profile-pic {
            width: 150px;
            height: 150px;
        }
        .main-title {
            text-align: center;
        }
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# 0. Cabeçalho (Apresentação)
# -----------------------------------------------------------------------------
col1, col2 = st.columns([1, 3], gap="large")

with col1:
    # Centraliza a foto visualmente no mobile usando uma div CSS
    st.markdown(
        f'<div class="profile-pic-container"><img src="data:image/png;base64,{img_base64}" class="profile-pic"></div>', 
        unsafe_allow_html=True
    )

with col2:
    # Título e Subtítulo baseados na sua trajetória profissional
    st.markdown('<div class="main-title">', unsafe_allow_html=True)
    st.title("Simone Alves Diana")

    # -----------------------------------------------------------------------------
    # 1. Hero Section (Apresentação)
    # -----------------------------------------------------------------------------
    st.subheader("Data Engineer | MLOps | AI Solutions")
    st.markdown("Mais de 25 anos de vivência na área de tecnologia atuando em soluções escaláveis de Engenharia de Dados, MLOps e IA Aplicada para negócios.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Botões Responsivos
    # No mobile, o use_container_width=True garante que ocupem a largura total se necessário
    col_btn1, col_btn2, _ = st.columns([1, 1, 1])
    with col_btn1:
        if st.button("Ver Projetos", type="primary", use_container_width=True):
            # Injeta o JS para rolar até o ID 'vitrine-projetos'
            st.components.v1.html(
                """
                <script>
                    var container = window.parent.document.getElementById('vitrine-projetos');
                    if (container) {
                        container.scrollIntoView({behavior: 'smooth', block: 'start'});
                    }
                </script>
                """,
                height=0,
            )
    with col_btn2:
        # Lendo o arquivo PDF
        with open("CurriculoSimoneAlvesDiana_Fev2026.pdf", "rb") as file:
            btn = st.download_button(
                label="Download CV",
                data=file,
                file_name="Curriculo Simone Alves Diana-Fev2026.pdf",
                mime="application/pdf",
                use_container_width=True
            )

    st.write("") # Espaçamento

st.divider()

# -----------------------------------------------------------------------------
# 2. Experiência e Educação (Linha do Tempo)
# -----------------------------------------------------------------------------
st.subheader("Trajetória Profissional")

st.markdown("""
<div class="timeline-item">
    <h4 style="margin-bottom:0;">Início de Carreira (1996 – 2007)</h4>
    <p style="color: #A1A1AA; font-size: 0.9rem;">Consolidação Técnica</p>
    <ul>
        <li>Souza Aranha e Intermédica: Iniciei como Analista Júnior e Pleno, focando em modelagem de dados e projetos de Database Marketing para grandes clientes como Tecnologia Bancária e Casas Pernambucanas.</li>
        <li>Novabase (VIVO e Experiência Internacional): Atuei como Consultora BI Sênior. Na VIVO, coordenei equipes técnicas em projetos de Customer Lifetime Management e processos de ETL em larga escala.</li>
        <li>Entre 2004 e 2005, tive uma experiência internacional em Portugal no Banco Espírito Santo pela Novabase, desenhando modelos dimensionais para indicadores financeiros.</li>
    </ul>
</div>
<div class="timeline-item">
    <h4 style="margin-bottom:0;">Consultoria Estratégica (2007 – 2015)</h4>
    <p style="color: #A1A1AA; font-size: 0.9rem;">Especialização em BI</p>
    <ul>
        <li>IBM: Como Consultora Sênior, liderei tecnicamente projetos de Business Intelligence e Business Strategy para os maiores bancos do país (Itaú, Santander e Bradesco).</li>
        <li>Foi responsável pela arquitetura de soluções, modelagem lógica e física em projetos de Data Warehouse e Data Marts, e por desenho e especificação dos processos de integração e conversão das bases de dados durante a fusão entre os bancos Santander e Real.</li>
    </ul>
</div>
<div class="timeline-item">
    <h4 style="margin-bottom:0;">Liderança em Transformação Digital e Agilidade (2015 – 2024)</h4>
    <p style="color: #A1A1AA; font-size: 0.9rem;">Sistemas de Informação</p>
    <ul>
        <li>Banco Original / BSI Tecnologia: Atuei como Especialista em BI, Gerente de Projetos e Tech Lead. Gerenciei a implantação de soluções de CRM e Big Data, integrando dados transacionais com ferramentas de Web Analytics (Adobe e AppsFlyers) sob metodologias ágeis (Scrum e Kanban).</li>
        <li>PicPay Bank: Atuei como Tech Manager nas Squads de "Decisão de Crédito On-Line". Liderei a migração de sistemas On-Premise para a nuvem AWS, utilizando Java para reconstrução de regras de negócio e aplicando práticas de DevOps e métricas DORA para gestão de performance.</li>
    </ul>
</div>
<div class="timeline-item">
    <h4 style="margin-bottom:0;">Formação e Transição Atual para IA</h4>
    <p style="color: #A1A1AA; font-size: 0.9rem;">Presente</p>
    <ul>
        <li>Formação Acadêmica: Bacharel em Ciência da Computação (USJT) com MBA Executivo em TI pela ESPM.</li>
        <li>Foco em Inovação: Atualmente, estou expandindo meu portfólio para IA Generativa, Machine Learning e Microsoft Fabric, com certificações em curso pela Microsoft, Stanford e Alura, visando aplicar Inteligência Artificial em engenharia de dados e decisões estratégicas de negócios.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# -----------------------------------------------------------------------------
# 3. Tech Stack & Ferramentas
# -----------------------------------------------------------------------------
st.subheader("Tech Stack")
t_col1, t_col2, t_col3, t_col4 = st.columns(4)

with t_col1:
    st.markdown("**Cloud & DevOps**\n- ☁️ Microsoft Azure\n- ☁️ AWS (Amazon Web Services)\n- ♾️ Azure DevOps & GitHub Actions")
with t_col2:
    st.markdown("**Data & AI**\n- 🧠 Machine Learning\n- 🗣️ RAG & NLP\n- ⚙️ MLOps")
with t_col3:
    st.markdown("**Linguagens**\n- 🐍 Python\n- 🗄️ SQL Avançado")
with t_col4:
    st.markdown("**Bibliotecas & Ferramentas**\n- 🦜 LangChain\n- 👑 Streamlit\n- 💻 VSCode")

st.markdown("---")


# -----------------------------------------------------------------------------
# 4. Vitrine de Projetos (Bento Grid Style)
# -----------------------------------------------------------------------------

# Criamos uma âncora HTML com ID fixo para o JavaScript encontrar
st.markdown('<div id="vitrine-projetos"></div>', unsafe_allow_html=True)
st.subheader("Vitrine de Projetos")

b_col1, b_col2 = st.columns(2)

with b_col1:
    st.markdown("""
    <div class="bento-card">
        <h3 style="margin-top:0;">🧭 Bússola AI</h3>
        <p style="color: #A1A1AA;">Agente inteligente projetado para auxiliar na análise de crédito e oferecer orientação financeira embasada em dados estruturados. </p>
        <div>
            <span class="tag">Python</span>
            <span class="tag">LangChain</span>
            <span class="tag">Streamlit</span>
            <span class="tag">Groq</span>
            <span class="tag">FAISS</span>
            <span class="tag">LLM Google gemini</span>   
            <span class="tag">Google Generative AI Embeddings</span>
        </div>
        <br>
        <a href="https://github.com/SiDianaGit/dio-lab-bia" style="color: #60A5FA; text-decoration: none; margin-right: 20px;">GitHub ↗</a>
        <a href="https://dio-lab-bia-fefopyazarlmfz3u4abjyv.streamlit.app/" style="color: #60A5FA; text-decoration: none;">Live Demo ↗</a>
    </div>
    """, unsafe_allow_html=True)

#with b_col2:
#    st.markdown("""
#    <div class="bento-card">
#        <h3 style="margin-top:0;">☁️ Automação Cloud Native</h3>
#        <p style="color: #A1A1AA;">Scripts e pipelines desenvolvidos para orquestração de recursos serverless e governança de dados em nuvem, minimizando custos de infraestrutura.</p>
#        <div>
#            <span class="tag">AWS CLI</span>
#            <span class="tag">Boto3</span>
#            <span class="tag">Data Governance</span>
#        </div>
#        <br>
#        <a href="#" style="color: #60A5FA; text-decoration: none;">Repositório de Scripts ↗</a>
#    </div>
#    """, unsafe_allow_html=True)

st.markdown("---")


# -----------------------------------------------------------------------------
# 5. Formulário de Contato / Rodapé
# -----------------------------------------------------------------------------
st.subheader("Contato")
c_col1, c_col2 = st.columns([2, 1])

with c_col1:
    # URL do FormSubmit com o seu e-mail
    contact_form_url = "https://formsubmit.co/si_ap@hotmail.com"
    
    # Criando o formulário usando HTML para integração direta com o serviço de e-mail
    contact_form_html = f"""
    <form action="{contact_form_url}" method="POST">
        <input type="hidden" name="_subject" value="From My Portfolio">
        <input type="hidden" name="_captcha" value="false">
        <p style="margin-bottom: 10px;">Tem um projeto de dados desafiador? Vamos conversar.</p>
        <label style="display: block; margin-bottom: 5px;">Seu Nome</label>
        <input type="text" name="name" placeholder="Como posso te chamar?" style="width: 100%; margin-bottom: 15px; padding: 8px; border-radius: 5px; border: 1px solid #444; background: #1E1E1E; color: white;" required>
        <label style="display: block; margin-bottom: 5px;">Seu E-mail</label>
        <input type="email" name="email" placeholder="seu-email@exemplo.com" style="width: 100%; margin-bottom: 15px; padding: 8px; border-radius: 5px; border: 1px solid #444; background: #1E1E1E; color: white;" required>
        <label style="display: block; margin-bottom: 5px;">Mensagem</label>
        <textarea name="message" placeholder="Sua mensagem aqui..." style="width: 100%; height: 100px; margin-bottom: 15px; padding: 8px; border-radius: 5px; border: 1px solid #444; background: #1E1E1E; color: white;" required></textarea>
        <button type="submit" style="background-color: #FF4B4B; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; width: 100%;">Enviar Mensagem</button>
    </form>
    """
    
    st.markdown(contact_form_html, unsafe_allow_html=True)
       
        
    #if submitted:
    #    st.success("Mensagem enviada com sucesso! Entrarei em contato em breve.")

with c_col2:
    st.markdown("""
    **Links Rápidos**
    - [🔗 LinkedIn](https://www.linkedin.com/in/simone-diana)
    - [🐙 GitHub](https://github.com/SiDianaGit)
    - [▶️ YouTube](https://www.youtube.com/@DIANA-Digital-Insights)
    """)