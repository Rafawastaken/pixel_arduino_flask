const boxes = document.querySelectorAll(".cel");

boxes.forEach((box) => {
  box.addEventListener("click", function handleClick(event) {
    change_color(box);
    send_position(box);
  });
});

function change_color(box) {
  const current_color = box.getAttribute("class").split(" ")[1];
  if (current_color === "blank") {
    box.classList.remove("blank");
    box.classList.add("colored");
  }
  if (current_color === "colored") {
    box.classList.remove("colored");
    box.classList.add("blank");
  }
}

function send_position(box) {
  // console.log(box.getAttribute("aria-label"));
}
