document.addEventListener('DOMContentLoaded', function () {
                                const landingPageHead = document.querySelector('.landing-page-head');
                                const landingPageContents = document.querySelector('.landing-landing-para');
                                const landingPageButton = document.querySelector('.landing_page_btn');
                                const awardsSection = document.querySelector('.awards-sec1');
                                const placementHead = document.querySelector('.placement');
                                const galleriesHead = document.querySelector('.galleries');
                                const onEntry = function (entries, observer) {
                                entries.forEach(entry =&gt; {
                                if (entry.isIntersecting) {
                                entry.target.classList.add('inview');
                                }
                                });
                                };
                                const observer = new IntersectionObserver(onEntry, { threshold: 0.2 });

                                if (landingPageHead) observer.observe(landingPageHead);
                                if (landingPageContents) observer.observe(landingPageContents);
                                if (landingPageButton) observer.observe(landingPageButton);
                                if (awardsSection) observer.observe(awardsSection);
                                if (placementHead) observer.observe(placementHead);
                                if (galleriesHead) observer.observe(galleriesHead);

                                });