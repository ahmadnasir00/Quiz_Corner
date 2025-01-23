document.addEventListener('DOMContentLoaded', function() {
    const questionsContainer = document.getElementById('questions-container');
    const addQuestionBtn = document.getElementById('add-question-btn');
    
    // Add question button handler
    addQuestionBtn.addEventListener('click', function() {
        const questionCount = questionsContainer.querySelectorAll('.question-section').length;
        const newQuestion = createQuestionElement(questionCount);
        questionsContainer.appendChild(newQuestion);
    });

    // Delete question handler (delegated)
    questionsContainer.addEventListener('click', function(e) {
        if (e.target.classList.contains('delete-question-btn')) {
            const questionSection = e.target.closest('.question-section');
            if (questionSection && confirm('Are you sure you want to delete this question?')) {
                questionSection.remove();
            }
        }
    });

    // Add choice handler (delegated)
    questionsContainer.addEventListener('click', function(e) {
        if (e.target.classList.contains('add-choice-btn')) {
            const questionSection = e.target.closest('.question-section');
            if (questionSection) {
                const choicesList = questionSection.querySelector('.choices-list');
                const questionIndex = Array.from(questionsContainer.children).indexOf(questionSection);
                const choiceCount = choicesList.querySelectorAll('.choice-item').length;
                const newChoice = createChoiceElement(questionIndex, choiceCount);
                choicesList.appendChild(newChoice);
            }
        }
    });

    // Delete choice handler (delegated)
    questionsContainer.addEventListener('click', function(e) {
        if (e.target.classList.contains('delete-choice-btn')) {
            const choiceItem = e.target.closest('.choice-item');
            if (choiceItem && confirm('Are you sure you want to delete this choice?')) {
                choiceItem.remove();
            }
        }
    });

    function createQuestionElement(index) {
        const template = `
            <div class="question-section card mb-3">
                <div class="card-body">
                    <div class="d-flex justify-content-between align-items-center mb-3">
                        <h5 class="card-title">Question ${index + 1}</h5>
                        <button type="button" class="btn btn-danger delete-question-btn" title="Delete Question">
                            <i class="bi bi-trash-fill"></i>
                        </button>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Question Text</label>
                        <textarea class="form-control question-text" 
                                  name="questions[${index}][text]" 
                                  required></textarea>
                    </div>
                    <div class="choices-container mb-3">
                        <div class="choices-list">
                            ${createChoiceElement(index, 0).outerHTML}
                        </div>
                        <button type="button" class="btn btn-success add-choice-btn">
                            <i class="bi bi-plus-circle-fill"></i> Add Choice
                        </button>
                    </div>
                </div>
            </div>
        `;
        return document.createRange().createContextualFragment(template).firstElementChild;
    }

    function createChoiceElement(questionIndex, choiceIndex) {
        const template = `
            <div class="choice-item mb-2">
                <div class="input-group">
                    <input type="text" class="form-control" 
                           name="questions[${questionIndex}][choices][${choiceIndex}][text]" 
                           placeholder="Choice text" required>
                    <div class="input-group-text">
                        <input class="form-check-input" type="radio" 
                               name="questions[${questionIndex}][correct_choice]" 
                               value="${choiceIndex}" required>
                    </div>
                    <button type="button" class="btn btn-danger delete-choice-btn" title="Delete Choice">
                        <i class="bi bi-trash3-fill"></i>
                    </button>
                </div>
            </div>
        `;
        return document.createRange().createContextualFragment(template).firstElementChild;
    }
});
