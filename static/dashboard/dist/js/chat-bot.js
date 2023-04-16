function chatToggler() {
    let chatSohbet = document.querySelector('#chat-sohbet');
    chatSohbet.classList.toggle('active');
}
const pairs = [
    ['Bu sistem ne ise yariyir',['Sizin suallariniza cavab verir', 'bekarciliqdi']],
    ['Oglansan?', ['nem','Tuncaydan ferqli olaraq he']],
    ['Seni kim dogub?',[ 'Atasiz Anasiz Cansiz insanam', 'sen']],
    ['Sagol', ['sag olma ayqa','Sagol ayqa']]
];

function chatbot(){
    const input = document.getElementById('textarea1').value;
    const output = document.getElementById('chatlist');
    const result = pairs.find(pair => {
        const pattern = new RegExp(pair[0], 'i');
        return pattern.test(input);
    });
    const response = result ? result[1][Math.floor(Math.random() * result[1].length)] : "I'm sorry";
    output.innerHTML += "<li class='chat-item'><div class='chat-img'><img src='{% static '/dashboard/assets/images/users/1.jpg' %}' alt='user' /></div><div class='chat-content'><h6 class='font-medium'>ChatBot</h6><div class='box bg-light-info me-5'>" 
    + response +
    '</div></div><div class="chat-time">' + saat + ':' + deq +
    '</div></li>'    
}




const vaxt = new Date();
let saat = vaxt.getHours();
let deq = vaxt.getMinutes();
if (deq<=9) {
    deq = "0" +deq
}
if (saat<=9) {
    saat = "0" +saat
}
 let a;
function send() {
    let text = document.getElementById('textarea1');
    let chatList = document.getElementById('chatlist');
    chatlist.innerHTML += '<li class="odd chat-item"><div class="chat-content"><div class="box bg-light-inverse ml-5">' 
    + text.value +
    '</div></div><div class="chat-time">' + saat + ':' + deq +
    '</div></li>'    
    text.value= "";
    chatbot();

}