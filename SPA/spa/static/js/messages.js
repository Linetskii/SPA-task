"use strict";

function showForm(id) {
    const formDOM = document.getElementById("form-" + id);
    if (formDOM.style.display === "flex") {
        formDOM.style.display = "none";
    } else {
        formDOM.style.display = "flex";
    };
};

function insertSimple(id, tag) {
    let messageText = document.getElementById("form-" + id).getElementsByTagName('textarea')[0];
    let to = messageText.selectionEnd;
    messageText.value = messageText.value.substring(0, to) + '</' + tag + '>\r\n' + messageText.value.substring((to));
    messageText.focus();
    // select the content
    messageText.setSelectionRange((to + tag.length + 3), (to + tag.length + 3));
};

function insertTag(id, tag) {
    let messageText = document.getElementById("form-" + id).getElementsByTagName('textarea')[0];
    let from = messageText.selectionStart;
    let to = messageText.selectionEnd;
    let selectedText = messageText.value.substring(from, to);
    messageText.value = messageText.value.substring(0, from) + '<' + tag + '>' + selectedText + '</' + tag + '>' + messageText.value.substring(to);
    messageText.focus();
    // select the content
    messageText.setSelectionRange((from + tag.length + 2), (to + tag.length + 2));
};

function insertRef(id) {
    let messageText = document.getElementById("form-" + id).getElementsByTagName('textarea')[0];
    let from = messageText.selectionStart;
    let to = messageText.selectionEnd;
    let selectedText = messageText.value.substring(from, to);
    messageText.value = messageText.value.substring(0, from) + '<a href="' + selectedText + '"></a>' + messageText.value.substring(to);
    messageText.focus();
    // set the caret between tags
    messageText.setSelectionRange((11 + to), (11 + to));
};

function previewMessage(id) {
    const previewDiv = document.getElementById("preview-" + id);
    const messageText = document.getElementById("form-" + id).getElementsByTagName('textarea')[0];
    messageText.focus();
    messageText.select();
    previewDiv.innerHTML = ""
    previewDiv.insertAdjacentHTML(
            "afterbegin",
            `<div class=message>${messageText.value}</div>`
        );
};

function expandImg(file) {
    document.body.insertAdjacentHTML(
        "afterbegin",
        `<img class="full-img" src="${file}">`
        )
};

function expandImg(file) {
    const outer = document.getElementById("outer");
    outer.innerHTML = `<img id="preview" class="full-img" src="${file}">`;
    outer.style.display = "block";
};

function clearPreview() {
    outer = document.getElementById('outer');
    outer.style.display = "none";
};

function sortBy() {
    let ordering = "";
    if (document.getElementById('order').checked === true) {
        ordering = "-";
    }
    const sort = document.getElementById('srt').value;
    const currentUrl = window.location.href.split("?")[0];
    const url = currentUrl + "?page=1&ordering=" + ordering + sort;
    window.open(url, "_self");
}