#!/usr/bin/nodejs
const redHeader = document.querySelector('div#red_header');
redHeader.addEventListener('click', function () {
  document.querySelector('header').style.color = '#FF0000';
});
