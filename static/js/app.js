// DOM Elements
const imageInput = document.getElementById("imageInput");
const previewContainer = document.getElementById("previewContainer");
const previewImage = document.getElementById("previewImage");

const predictBtn = document.getElementById("predictBtn");

const predictionSection = document.getElementById("predictionSection");
const animalName = document.getElementById("animalName");
const uploadedImage = document.getElementById("uploadedImage");

const chatSection = document.getElementById("chatSection");
const chatMessages = document.getElementById("chatMessages");
const questionInput = document.getElementById("questionInput");
const sendBtn = document.getElementById("sendBtn");

const loading = document.getElementById("loading");
const errorBox = document.getElementById("errorBox");

const newImageBtn = document.getElementById("newImageBtn");
const resetContainer = document.getElementById("resetContainer");

// ==============================

let selectedFile = null;
let currentSpecies = null;

// ==============================

function showLoading() {
    loading.classList.remove("hidden");
}

function hideLoading() {
    loading.classList.add("hidden");
}

function showError(message) {

    errorBox.innerText = message;
    errorBox.classList.remove("hidden");

    setTimeout(() => {
        errorBox.classList.add("hidden");
    }, 4000);

}

function scrollChatBottom() {

    chatMessages.scrollTop = chatMessages.scrollHeight;

}

// Image Preview
imageInput.addEventListener("change", (event) => {

    const file = event.target.files[0];

    if (!file)
        return;

    selectedFile = file;

    previewImage.src = URL.createObjectURL(file);

    previewContainer.classList.remove("hidden");

    predictBtn.disabled = false;

});

// Predict
predictBtn.addEventListener("click", async () => {

    if (!selectedFile)
        return;

    showLoading();

    const formData = new FormData();

    formData.append("image", selectedFile);

    try {

        const response = await fetch(API.predict, {

            method: "POST",

            body: formData

        });

        console.log("response is: ", response);

        if (!response.ok)
            throw new Error("Prediction failed.");

        const data = await response.json();

        currentSpecies = data.species;

        animalName.innerHTML = "🐾 " + data.species;

        uploadedImage.src = data.image;

        predictionSection.classList.remove("hidden");

        chatSection.classList.remove("hidden");

        resetContainer.classList.remove("hidden");

        chatMessages.innerHTML = "";

        addBotMessage(
            `Hello 👋

I identified the animal as ${data.species}.

You can ask me:

• What does it eat?

• Where does it live?

• Scientific name

• Weight

• Speed

• Lifespan

• Interesting fact`
        );

    } catch (err) {

        console.error(err);

        showError(err.message);

    }

    hideLoading();

});

// Send Question
async function sendQuestion() {

    const question = questionInput.value.trim();

    if (question === "")
        return;

    if (!currentSpecies)
        return;

    addUserMessage(question);

    questionInput.value = "";

    showLoading();

    try {

        const response = await fetch(API.chat, {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                species: currentSpecies,

                question: question

            })

        });

        if (!response.ok)
            throw new Error("Unable to contact chatbot.");

        const data = await response.json();

        addBotMessage(data.answer);

    } catch (err) {

        console.error(err);

        showError(err.message);

    }

    hideLoading();

}

sendBtn.addEventListener("click", sendQuestion);

questionInput.addEventListener("keydown", (e) => {

    if (e.key === "Enter") {

        e.preventDefault();

        sendQuestion();

    }

});

// Chat Messages

function addUserMessage(message) {

    const div = document.createElement("div");

    div.className = "message user";

    div.innerHTML = `

        <div class="bubble">

            ${message}

        </div>

    `;

    chatMessages.appendChild(div);

    scrollChatBottom();

}

function addBotMessage(message) {

    const div = document.createElement("div");

    div.className = "message bot";

    div.innerHTML = `

        <div class="bubble">

            ${message}

        </div>

    `;

    chatMessages.appendChild(div);

    scrollChatBottom();

}

// Reset

newImageBtn.addEventListener("click", () => {

    currentSpecies = null;

    selectedFile = null;

    imageInput.value = "";

    previewImage.src = "";

    uploadedImage.src = "";

    questionInput.value = "";

    animalName.innerHTML = "";

    chatMessages.innerHTML = "";

    previewContainer.classList.add("hidden");

    predictionSection.classList.add("hidden");

    chatSection.classList.add("hidden");

    resetContainer.classList.add("hidden");

    predictBtn.disabled = true;

});