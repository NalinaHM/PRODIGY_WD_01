/* ==========================================================================
   PRODIGY INFOTECH - TASK 01: INTERACTIVE NAVIGATION & LANDING ENGINE
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  const navbar = document.getElementById('navbar');
  const navLinks = document.querySelectorAll('.nav-link');
  const sections = document.querySelectorAll('section[id]');
  const hamburger = document.getElementById('hamburger');
  const navMenu = document.getElementById('navMenu');

  // Scroll Monitor Elements
  const scrollPosVal = document.getElementById('scrollPosVal');
  const navStateVal = document.getElementById('navStateVal');
  const activeSecVal = document.getElementById('activeSecVal');

  // 1. Navbar Scroll Interaction Engine (Fixed position + style change on scroll)
  const handleScroll = () => {
    const scrollY = window.scrollY;

    // Update Monitor
    if (scrollPosVal) scrollPosVal.textContent = `${Math.round(scrollY)} px`;

    if (scrollY > 50) {
      navbar.classList.add('scrolled');
      if (navStateVal) {
        navStateVal.textContent = 'Scrolled Glassmorphism';
        navStateVal.style.background = 'rgba(6, 182, 212, 0.15)';
        navStateVal.style.color = 'var(--secondary)';
      }
    } else {
      navbar.classList.remove('scrolled');
      if (navStateVal) {
        navStateVal.textContent = 'Transparent Header';
        navStateVal.style.background = 'rgba(99, 102, 241, 0.15)';
        navStateVal.style.color = 'var(--primary)';
      }
    }

    // Active Link Highlighting based on visible section
    let currentSection = '';
    const scrollPosition = scrollY + 160;

    sections.forEach(section => {
      const top = section.offsetTop;
      const height = section.offsetHeight;
      if (scrollPosition >= top && scrollPosition < top + height) {
        currentSection = section.getAttribute('id');
      }
    });

    if (currentSection && activeSecVal) {
      activeSecVal.textContent = `#${currentSection}`;
    }

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${currentSection}`) {
        link.classList.add('active');
      }
    });
  };

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll(); // Initial call

  // 2. Mobile Hamburger Drawer Toggle
  if (hamburger && navMenu) {
    hamburger.addEventListener('click', () => {
      navMenu.classList.toggle('active');
      hamburger.classList.toggle('active');
    });

    // Close mobile menu on link click
    navLinks.forEach(link => {
      link.addEventListener('click', () => {
        navMenu.classList.remove('active');
        hamburger.classList.remove('active');
      });
    });
  }

  // 3. Theme Studio Color Switcher
  const themeBtns = document.querySelectorAll('.theme-btn');
  themeBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      themeBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const theme = btn.dataset.theme;
      document.body.setAttribute('data-theme', theme);
    });
  });

  // 4. FAQ Accordion Toggle Logic
  const accordionHeaders = document.querySelectorAll('.accordion-header');
  accordionHeaders.forEach(header => {
    header.addEventListener('click', () => {
      const item = header.parentElement;
      const isActive = item.classList.contains('active');

      // Close all accordion items
      document.querySelectorAll('.accordion-item').forEach(i => i.classList.remove('active'));

      // Toggle current item
      if (!isActive) {
        item.classList.add('active');
      }
    });
  });

  // Open first FAQ item by default
  const firstFaq = document.querySelector('.accordion-item');
  if (firstFaq) firstFaq.classList.add('active');

  // 5. Form Validation & Toast Notification
  const contactForm = document.getElementById('contactForm');
  const formToast = document.getElementById('formToast');

  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('nameInput').value.trim();
      const email = document.getElementById('emailInput').value.trim();
      const message = document.getElementById('messageInput').value.trim();

      if (!name || !email || !message) {
        showToast('Please complete all required fields.', 'error');
        return;
      }

      showToast('🚀 Thank you! Your message has been sent successfully.', 'success');
      contactForm.reset();
    });
  }

  function showToast(msg, type) {
    if (!formToast) return;
    formToast.textContent = msg;
    formToast.style.display = 'block';

    if (type === 'success') {
      formToast.style.background = 'rgba(16, 185, 129, 0.15)';
      formToast.style.color = '#10b981';
      formToast.style.border = '1px solid rgba(16, 185, 129, 0.3)';
    } else {
      formToast.style.background = 'rgba(239, 68, 68, 0.15)';
      formToast.style.color = '#ef4444';
      formToast.style.border = '1px solid rgba(239, 68, 68, 0.3)';
    }
  }
});
