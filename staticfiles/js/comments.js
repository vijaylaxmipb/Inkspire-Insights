/* jshint esversion: 6 */
/* global bootstrap */

document.addEventListener("DOMContentLoaded", () => {
  console.log("comments.js loaded");

  const deleteModalElement = document.getElementById("deleteModal");
  console.log("Delete modal element found:", deleteModalElement);
  

  if (!deleteModalElement) {
      console.error("Delete modal element not found!");
      return;
  }

  const deleteModal = new bootstrap.Modal(deleteModalElement);
  const deleteButtons = document.getElementsByClassName("btn-delete");
  const deleteConfirm = document.getElementById("deleteConfirm");

  if (!deleteConfirm) {
      console.error("Delete confirmation button not found!");
      return;
  }

  for (let button of deleteButtons) {
      button.addEventListener("click", (e) => {
          const commentId = e.target.getAttribute("comment_id");
          console.log("Comment ID:", commentId);
 
          if (commentId) {
              deleteConfirm.href = `/delete_comment/${commentId}`;
              deleteModal.show();
          } else {
              console.error("Comment ID is missing!");
          }
      });
  }
});
 
  // Edit comment functionality
  const editButtons = document.getElementsByClassName("btn-edit");
  const commentText = document.getElementById("id_body");
  const commentForm = document.getElementById("commentForm");
  const submitButton = document.getElementById("submitButton");
  
  for (let button of editButtons) {
    button.addEventListener("click", (e) => {
      const commentId = e.target.getAttribute("comment_id");
      const commentContent = document.getElementById(`comment${commentId}`).innerText;
      commentText.value = commentContent;
      submitButton.innerText = "Update";
      commentForm.setAttribute("action", `edit_comment/${commentId}`);
    });
  }
  
