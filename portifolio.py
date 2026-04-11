import streamlit as st

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
        -webkit-text-fill-color: transparent;
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
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 1. Hero Section (Apresentação)
# -----------------------------------------------------------------------------
st.markdown('<div class="hero-title">Data Engineer & Cloud Architect.</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">Traduzindo mais de 25 anos de vivência em TI corporativa em soluções escaláveis de Engenharia de Dados, MLOps e IA Aplicada para negócios.</div>', unsafe_allow_html=True)

col_btn1, col_btn2, _ = st.columns([1, 1, 4])
with col_btn1:
    st.button("Ver Projetos", type="primary", use_container_width=True)
with col_btn2:
    st.button("Download CV", use_container_width=True)

st.write("") # Espaçamento
st.markdown("---")

# -----------------------------------------------------------------------------
# 2. Vitrine de Projetos (Bento Grid Style)
# -----------------------------------------------------------------------------
st.subheader("Vitrine de Projetos")

b_col1, b_col2 = st.columns(2)

with b_col1:
    st.markdown("""
    <div class="bento-card">
        <h3 style="margin-top:0;">🧭 Bússola AI</h3>
        <p style="color: #A1A1AA;">Agente inteligente projetado para auxiliar na análise de crédito e oferecer orientação financeira embasada em dados estruturados.</p>
        <div>
            <span class="tag">Python</span>
            <span class="tag">LangChain</span>
            <span class="tag">Streamlit</span>
            <span class="tag">Azure</span>
            <span class="tag">NLP</span>
        </div>
        <br>
        <a href="#" style="color: #60A5FA; text-decoration: none; margin-right: 20px;">GitHub ↗</a>
        <a href="#" style="color: #60A5FA; text-decoration: none;">Live Demo ↗</a>
    </div>
    """, unsafe_allow_html=True)

with b_col2:
    st.markdown("""
    <div class="bento-card">
        <h3 style="margin-top:0;">☁️ Automação Cloud Native</h3>
        <p style="color: #A1A1AA;">Scripts e pipelines desenvolvidos para orquestração de recursos serverless e governança de dados em nuvem, minimizando custos de infraestrutura.</p>
        <div>
            <span class="tag">AWS CLI</span>
            <span class="tag">Boto3</span>
            <span class="tag">Data Governance</span>
        </div>
        <br>
        <a href="#" style="color: #60A5FA; text-decoration: none;">Repositório de Scripts ↗</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# -----------------------------------------------------------------------------
# 3. Experiência e Educação (Linha do Tempo)
# -----------------------------------------------------------------------------
st.subheader("Trajetória Profissional")

st.markdown("""
<div class="timeline-item">
    <h4 style="margin-bottom:0;">Engenharia de Dados, MLOps e IA Aplicada</h4>
    <p style="color: #A1A1AA; font-size: 0.9rem;">Presente</p>
    <ul>
        <li>Desenvolvimento de pipelines de dados e agentes de Inteligência Artificial usando RAG, Tokenização e Embeddings.</li>
        <li>Arquitetura e provisionamento de soluções em nuvem utilizando Microsoft Azure e AWS.</li>
        <li>Foco na transição para governança de dados avançada e operações de Machine Learning (MLOps).</li>
    </ul>
</div>
<div class="timeline-item">
    <h4 style="margin-bottom:0;">Especialista em Business Intelligence & Transformação Digital</h4>
    <p style="color: #A1A1AA; font-size: 0.9rem;">25+ Anos de Experiência em TI</p>
    <ul>
        <li>Mais de duas décadas atuando fortemente em modelagem, tratamento e entrega de dados estruturados para tomadores de decisão.</li>
        <li>Liderança na transformação digital corporativa através da implementação de sistemas robustos e governança sistêmica.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# -----------------------------------------------------------------------------
# 4. Tech Stack & Ferramentas
# -----------------------------------------------------------------------------
st.subheader("Tech Stack")
t_col1, t_col2, t_col3, t_col4 = st.columns(4)

with t_col1:
    st.markdown("**Cloud & DevOps**\n- ☁️ Microsoft Azure\n- ☁️ AWS (Amazon Web Services)\n- ♾️ Azure DevOps")
with t_col2:
    st.markdown("**Data & AI**\n- 🧠 Machine Learning\n- 🗣️ RAG & NLP\n- ⚙️ MLOps")
with t_col3:
    st.markdown("**Linguagens**\n- 🐍 Python\n- 🗄️ SQL Avançado")
with t_col4:
    st.markdown("**Bibliotecas & Ferramentas**\n- 🦜 LangChain\n- 👑 Streamlit\n- 📄 PyPDF2\n- 💻 VSCode")

st.markdown("---")

# -----------------------------------------------------------------------------
# 5. Formulário de Contato / Rodapé
# -----------------------------------------------------------------------------
st.subheader("Contato")
c_col1, c_col2 = st.columns([2, 1])

with c_col1:
    with st.form("contact_form", clear_on_submit=True):
        st.write("Tem um projeto de dados desafiador? Vamos conversar.")
        st.text_input("Seu Nome")
        st.text_input("Seu E-mail")
        st.text_area("Mensagem", height=100)
        submitted = st.form_submit_button("Enviar Mensagem")
        if submitted:
            st.success("Mensagem enviada com sucesso! Entrarei em contato em breve.")

with c_col2:
    st.markdown("""
    **Links Rápidos**
    - [🔗 LinkedIn](#)
    - [🐙 GitHub](#)
    - [▶️ YouTube (NextCode.AI)](#)
    """)