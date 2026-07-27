/* ==========================================================================
   TASK-04: DEVELOPER PORTFOLIO ENGINE & INTERACTIVE FILTERS
   ========================================================================== */

export function initPortfolio() {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const projectCards = document.querySelectorAll('.portfolio-project-card');
  const contactForm = document.getElementById('portfolioContactForm');
  const formFeedback = document.getElementById('formFeedback');

  // 1. Project Category Filtering
  if (filterBtns.length > 0 && projectCards.length > 0) {
    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        // Active tab state
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        const category = btn.dataset.filter;

        projectCards.forEach(card => {
          if (category === 'all' || card.dataset.category === category) {
            card.style.display = 'block';
            card.style.opacity = '1';
            card.style.transform = 'scale(1)';
          } else {
            card.style.opacity = '0';
            card.style.transform = 'scale(0.95)';
            setTimeout(() => {
              if (card.dataset.category !== category && category !== 'all') {
                card.style.display = 'none';
              }
            }, 200);
          }
        });
      });
    });
  }

  // 2. Contact Form Handler & Validation
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('contactName')?.value.trim();
      const email = document.getElementById('contactEmail')?.value.trim();
      const message = document.getElementById('contactMessage')?.value.trim();

      if (!name || !email || !message) {
        showFeedback('Please fill out all fields.', 'error');
        return;
      }

      if (!validateEmail(email)) {
        showFeedback('Please enter a valid email address.', 'error');
        return;
      }

      showFeedback('🚀 Message sent successfully! Thank you for reaching out.', 'success');
      contactForm.reset();
    });
  }

  function validateEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }

  function showFeedback(msg, type) {
    if (!formFeedback) return;
    formFeedback.textContent = msg;
    formFeedback.style.display = 'block';
    formFeedback.style.padding = '0.75rem';
    formFeedback.style.borderRadius = 'var(--radius-sm)';
    formFeedback.style.marginTop = '1rem';
    formFeedback.style.fontWeight = '600';

    if (type === 'success') {
      formFeedback.style.background = 'rgba(16, 185, 129, 0.15)';
      formFeedback.style.color = 'var(--accent-emerald)';
      formFeedback.style.border = '1px solid rgba(16, 185, 129, 0.3)';
    } else {
      formFeedback.style.background = 'rgba(239, 68, 68, 0.15)';
      formFeedback.style.color = '#ef4444';
      formFeedback.style.border = '1px solid rgba(239, 68, 68, 0.3)';
    }
  }
}
