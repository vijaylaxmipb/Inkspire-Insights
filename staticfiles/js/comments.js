// Utility function to get CSRF token
function getCSRFToken() {
  const cookieValue = document.cookie
      .split('; ')
      .find(row => row.startsWith('csrftoken='))
      ?.split('=')[1];
  return cookieValue;
}

// Function to handle like button clicks
function handleLike(button) {
  const commentId = button.getAttribute("data-comment-id");
  fetch(`/like_comment/${commentId}/`, {
      method: "POST",
      headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCSRFToken(),
      },
  })
      .then((response) => response.json())
      .then((data) => {
          if (data.success) {
              const likeCountSpan = button.querySelector(".like-count");
              likeCountSpan.textContent = data.like_count; // Update like count
          } else {
              console.error("Failed to like comment:", data.error);
          }
      })
      .catch((error) => {
          console.error("Error liking comment:", error);
      });
}

// Attach event listeners to like buttons
document.querySelectorAll(".btn-like").forEach((button) => {
  button.addEventListener("click", () => {
      handleLike(button);
  });
});


// Attach event listeners to all like buttons
document.querySelectorAll(".btn-like").forEach((button) => {
  button.addEventListener("click", () => handleLike(button));
});

const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");
const likeButtons = document.querySelectorAll(".btn-like");

for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");
    let commentContent = document.getElementById(`comment${commentId}`).innerText;
    commentText.value = commentContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_comment/${commentId}`);
  });
}

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let commentId = e.target.getAttribute("comment_id");
      deleteConfirm.href = `delete_comment/${commentId}`;
      deleteModal.show();
    });
  }

