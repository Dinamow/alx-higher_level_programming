#!/usr/bin/nodejs
const redHeaderDiv = document.querySelector('#red_header');
header = document.querySelector('header');

redHeaderDiv.addEventListener('click', function () {
  header.classList.add('red');
});
