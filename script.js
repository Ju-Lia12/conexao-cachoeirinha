// Importa módulos do Firebase
import { initializeApp } from "https://www.gstatic.com/firebasejs/12.3.0/firebase-app.js";
import { getFirestore, collection, addDoc } from "https://www.gstatic.com/firebasejs/12.3.0/firebase-firestore.js";

// Configuração do Firebase
const firebaseConfig = {
  apiKey: "AIzaSyAGwCdwQH2E_GbiErytqvKkuLxq7y9qdU",
  authDomain: "conexao-cachoeirinha-1f599.firebaseapp.com",
  projectId: "conexao-cachoeirinha-1f599",
  storageBucket: "conexao-cachoeirinha-1f599.firebasestorage.app",
  messagingSenderId: "101039233453",
  appId: "1:101039233453:web:264f9703c0f0d99450a924",
  measurementId: "G-4CMMVQ98N8"
};

// Inicializa Firebase e Firestore
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

// Função para enviar formulário
async function enviarFormulario() {
  const opcao = document.getElementById("opcao").value;
  const nome = document.getElementById("nome").value;
  const bairro = document.getElementById("bairro").value;
  const rua = document.getElementById("rua").value;
  const texto = document.getElementById("texto").value;

  const hoje = new Date();
  const mes = hoje.getMonth() + 1;
  const ano = hoje.getFullYear();
  const mesAno = `${mes.toString().padStart(2, '0')}/${ano}`; // Formato MM/AAAA

  const dados = { opcao, nome, bairro, rua, texto, mesAno }; 

  try {
    await addDoc(collection(db, "formularios"), dados);
    alert("Formulário enviado com sucesso!");
    document.getElementById("meuFormulario").reset();
  } catch (e) {
    console.error("Erro ao salvar: ", e);
    alert("Ocorreu um erro ao enviar. Tente novamente.");
  }
}

// Listener para o envio do formulário
document.getElementById("meuFormulario").addEventListener("submit", (e) => {
  e.preventDefault(); // evita reload da página
  enviarFormulario();
});
