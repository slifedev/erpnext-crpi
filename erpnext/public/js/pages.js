function headerCollapse() {
    const header = document.querySelector('header.header');
    const doc = document.documentElement;
    const wrapper = document.querySelector('div.wrapper.y-scroll-snap');
    if (header) {
      wrapper.addEventListener('scroll', function (event) {
        const top = (wrapper.pageYOffset || wrapper.scrollTop) - (wrapper.clientTop || 0);
        if (top >= 10) {
          header.classList.add('collapsed');
        } else {
          header.classList.remove('collapsed');
        }
      });
    }
  }
  
  function tabSwitcher() {
    const buttons = document.querySelectorAll('.content-switch button');
    const sections = document.querySelectorAll('.content-section');
  
    buttons.forEach(button => {
      button.addEventListener('click', function () {
        buttons.forEach(btn => btn.classList.remove('active'));
  
        this.classList.add('active');
  
        sections.forEach(section => section.classList.remove('active'));
  
        const target = this.getAttribute('data-target');
        document.getElementById(target).classList.add('active');
      });
    });
  }
  
  document.addEventListener('DOMContentLoaded', function () {
    headerCollapse();
    tabSwitcher();
  });