function revealLocation() {
  const input = document.getElementById("input").value;
  const output = document.getElementById("output");
  output.innerHTML = `Your location will be leaked! Have fun (while it lasts). ik its not ${input}.`;
}

document.getElementById("submit").addEventListener("click", revealLocation);
