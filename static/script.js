const btn = document.getElementById('sbmt-btn');
const form = document.getElementById('form');
const aadhar = document.getElementById('aadhar');

btn.onclick = function() {
    aadhar.classList.remove('inactive-class');
}