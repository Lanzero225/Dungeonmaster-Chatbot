import logo from "../assets/images/professional-logo.jpg";

function Home() {
  return (
    <>
      {/* Hero Section */}
      <section className="hero">
        <div className="hero-overlay"></div>
        <div className="container hero-content">
          <div className="hero-text animate-fade-in-up">
            <div className="logo-container">
              <img src={logo} alt="Professional Logo" className="hero-logo" />
            </div>
            <h1 className="hero-title">Welcome to my Portfolio</h1>
            <p className="hero-description">
              As a 4th year BS Computer Science student specializing in Data Science, I hope to make a meaningful impact
              using my skills and knowledge by harnessing data-driven insights to solve real-world problems for society.
            </p>
            <div className="hero-buttons">
              <a href="/portfolio" className="btn btn-primary">View Portfolio</a>
              <a href="/experience" className="btn btn-secondary">Learn More</a>
            </div>
          </div>
        </div>
      </section>

      {/* About Section */}
      <section className="about-section">
        <div className="container">
          <h2 className="section-title">About Me</h2>
          <p>
            I am a 4th year BS Computer Science student specializing in Data Science, driven by a passion for
            uncovering meaningful insights through data.
          </p><br></br>
          <p>
            Throughout my academic journey, I have cultivated a strong foundation in programming, analytics, and research, continuously exploring how technology and data can intersect to drive innovation. I value collaboration and curiosity, always striving to learn, adapt, and grow with every opportunity.
          </p><br></br>
          <p>
            Beyond academics, I take part in initiatives that encourage knowledge sharing and community engagement, aiming to inspire others to pursue technology as a force for good in shaping a more data-informed future.
          </p>
        </div>
            <div className="quick-links-grid">
        <div className="card">
            <svg className="card-icon" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M22 10v6M2 10l10-5 10 5-10 5z"/>
                <path d="M6 12v5c3 3 9 3 12 0v-5"/>
            </svg>
            <h3 className="card-title">Education</h3>
            <p className="card-description">Explore my academic background and qualifications</p>
            <a href="education.html" className="card-link">
                View Details
                <svg className="link-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M5 12h14M12 5l7 7-7 7"/>
                </svg>
            </a>
        </div>

        <div className="card">
            <svg className="card-icon" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="2" y="7" width="20" height="14" rx="2" ry="2"/>
                <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>
            </svg>
            <h3 className="card-title">Experience</h3>
            <p className="card-description">Discover my professional journey and achievements</p>
            <a href="experience.html" className="card-link">
                View Details
                <svg className="link-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M5 12h14M12 5l7 7-7 7"/>
                </svg>
            </a>
        </div>

        <div className="card">
            <svg className="card-icon" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="16 18 22 12 16 6"/>
                <polyline points="8 6 2 12 8 18"/>
            </svg>
            <h3 className="card-title">Skills</h3>
            <p className="card-description">See my technical and professional competencies</p>
            <a href="skills.html" className="card-link">
                View Details
                <svg className="link-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M5 12h14M12 5l7 7-7 7"/>
                </svg>
            </a>
        </div>

        <div className="card">
            <svg className="card-icon" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="12" cy="8" r="7"/>
                <polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/>
            </svg>
            <h3 className="card-title">Certifications</h3>
            <p className="card-description">Review my professional certifications and training</p>
            <a href="certifications.html" className="card-link">
                View Details
                <svg className="link-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M5 12h14M12 5l7 7-7 7"/>
                </svg>
            </a>
        </div>
    </div>
      </section>

      {/* Featured / Why Work With Me Section */}
      <section className="featured-section">
        <div className="container">
          <h2 className="section-title">Why Work With Me</h2>
          <p className = "section-description">I bring a unique combination of technical expertise, leadership experience, and passion for innovation.</p>
          <div className="features-grid">
            <div className="feature-card">
                    <div className="feature-icon">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <circle cx="12" cy="8" r="7"/>
                            <polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/>
                        </svg>
                    </div>
              <h3>Excellence</h3>
              <p>Committed to delivering high-quality results that exceed expectations.</p>
            </div>
            <div className="feature-card">
                    <div className="feature-icon">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>
                        </svg>
                    </div>
              <h3>Passion</h3>
              <p>Driven by genuine enthusiasm for technology and continuous improvement.</p>
            </div>
            <div className="feature-card">
                  <div className="feature-icon">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <rect x="2" y="7" width="20" height="14" rx="2" ry="2"/>
                            <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>
                        </svg>
                  </div>
              <h3>Adaptability</h3>
              <p>Quick to learn new tools, adapt to challenges, and thrive in collaborative environments.</p>
            </div>
          </div>
        </div>
      </section>
    </>
  );
}

export default Home;