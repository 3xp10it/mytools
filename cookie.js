// ==UserScript==
// @name         getcookie
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  get cookie with keyboard shortcut:`alt+c`
// @author       You
// @match        *://*/*
// @grant        none
// ==/UserScript==

function doc_keyUp(e) {
    if (e.altKey && e.keyCode==67) {
        // call your function to do the thing
        prompt('cookie',document.cookie);
        return false;
    }
}
document.addEventListener('keyup', doc_keyUp, false);
