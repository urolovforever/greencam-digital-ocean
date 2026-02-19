// DOM Elements
const gradientOrb = document.getElementById('gradientOrb');
const nav = document.getElementById('nav');
const heroStats = document.getElementById('heroStats');
const mobileMenuToggle = document.getElementById('mobileMenuToggle');
const navLinks = document.getElementById('navLinks');

// State
let countersVisible = false;
let mobileMenuOpen = false;

// Initialize
document.addEventListener('DOMContentLoaded', function() {
    setupEventListeners();
    setupIntersectionObserver();
    setupPartnersCarousel();
});

// Event Listeners
function setupEventListeners() {
    // Scroll event
    window.addEventListener('scroll', handleScroll);

    // Mouse move for gradient orb
    window.addEventListener('mousemove', handleMouseMove);

    // Mobile menu toggle
    if (mobileMenuToggle) {
        mobileMenuToggle.addEventListener('click', toggleMobileMenu);
    }

    // Close mobile menu when clicking on a link
    if (navLinks) {
        const links = navLinks.querySelectorAll('.nav-link');
        links.forEach(link => {
            link.addEventListener('click', () => {
                if (mobileMenuOpen) {
                    toggleMobileMenu();
                }
            });
        });
    }
}

// Toggle mobile menu
function toggleMobileMenu() {
    mobileMenuOpen = !mobileMenuOpen;
    mobileMenuToggle.classList.toggle('active');
    navLinks.classList.toggle('mobile-menu-open');
}

// Handle scroll
function handleScroll() {
    const scrollY = window.scrollY;

    if (scrollY > 50) {
        nav.classList.add('scrolled');
    } else {
        nav.classList.remove('scrolled');
    }
}

// Handle mouse move
function handleMouseMove(e) {
    if (gradientOrb) {
        gradientOrb.style.left = (e.clientX - 300) + 'px';
        gradientOrb.style.top = (e.clientY - 300) + 'px';
    }
}

// Setup Intersection Observer for counter animation
function setupIntersectionObserver() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !countersVisible) {
                countersVisible = true;
                animateCounters();
            }
        });
    }, { threshold: 0.3 });

    if (heroStats) {
        observer.observe(heroStats);
    }
}

// Animate counters
function animateCounters() {
    const targets = [47, 12, 89, 2.3];
    const duration = 2000;
    const steps = 60;
    const interval = duration / steps;

    let step = 0;
    const timer = setInterval(() => {
        step++;
        const animatedNumbers = targets.map(target =>
            Math.min(target, (target / steps) * step)
        );

        const stat0 = document.getElementById('stat0');
        const stat1 = document.getElementById('stat1');
        const stat2 = document.getElementById('stat2');
        const stat3 = document.getElementById('stat3');

        if (stat0) stat0.textContent = Math.round(animatedNumbers[0]) + '%';
        if (stat1) stat1.textContent = Math.round(animatedNumbers[1]) + 'K+';
        if (stat2) stat2.textContent = Math.round(animatedNumbers[2]);
        if (stat3) stat3.textContent = animatedNumbers[3].toFixed(1) + 'M';

        if (step >= steps) {
            clearInterval(timer);
        }
    }, interval);
}

// Setup Partners Carousel with touch support
function setupPartnersCarousel() {
    const carousel = document.querySelector('.partners-carousel');
    if (!carousel) return;

    let isDragging = false;
    let startX = 0;
    let scrollLeft = 0;
    let animationPaused = false;

    // Touch events for mobile swipe
    carousel.addEventListener('touchstart', (e) => {
        isDragging = true;
        startX = e.touches[0].pageX;
        carousel.style.animationPlayState = 'paused';
        animationPaused = true;
    }, { passive: true });

    carousel.addEventListener('touchmove', (e) => {
        if (!isDragging) return;
        const x = e.touches[0].pageX;
        const diff = startX - x;
        const currentTransform = getComputedStyle(carousel).transform;
        const matrix = new DOMMatrix(currentTransform);
        carousel.style.transform = `translateX(${matrix.m41 - diff}px)`;
        startX = x;
    }, { passive: true });

    carousel.addEventListener('touchend', () => {
        isDragging = false;
        // Resume animation after a short delay
        setTimeout(() => {
            if (animationPaused) {
                carousel.style.transform = '';
                carousel.style.animationPlayState = 'running';
                animationPaused = false;
            }
        }, 3000);
    });

    // Mouse events for desktop drag
    carousel.addEventListener('mousedown', (e) => {
        isDragging = true;
        startX = e.pageX;
        carousel.style.animationPlayState = 'paused';
        carousel.style.cursor = 'grabbing';
        animationPaused = true;
    });

    carousel.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        e.preventDefault();
        const x = e.pageX;
        const diff = startX - x;
        const currentTransform = getComputedStyle(carousel).transform;
        const matrix = new DOMMatrix(currentTransform);
        carousel.style.transform = `translateX(${matrix.m41 - diff}px)`;
        startX = x;
    });

    carousel.addEventListener('mouseup', () => {
        if (!isDragging) return;
        isDragging = false;
        carousel.style.cursor = 'grab';
        // Resume animation after a short delay
        setTimeout(() => {
            if (animationPaused) {
                carousel.style.transform = '';
                carousel.style.animationPlayState = 'running';
                animationPaused = false;
            }
        }, 3000);
    });

    carousel.addEventListener('mouseleave', () => {
        if (isDragging) {
            isDragging = false;
            carousel.style.cursor = 'grab';
            setTimeout(() => {
                if (animationPaused) {
                    carousel.style.transform = '';
                    carousel.style.animationPlayState = 'running';
                    animationPaused = false;
                }
            }, 3000);
        }
    });

    // Set initial cursor
    carousel.style.cursor = 'grab';
}
