var elements = document.getElementsByClassName("breakline")
console.log(elements)

for (i=0; i<elements.length; i++) {
  var text = elements[i].innerHTML;

  var displayText = text.replace(/\n/g, "<br />");

  elements[i].innerHTML = displayText
}
