import { useState } from "react";
import "./css/styles.css";
import "./css/animations.css";
import { Routes, Route } from "react-router-dom";
import Education from "./pages/Education";
import Home from "./pages/Home";
import { Link } from "react-router-dom";



function Navbar() {
  return (
    <nav className="navbar">
      <div className="nav-container">
        <Link to="/" className="nav-logo">Earl Tan Portfolio</Link>
        <div className="nav-menu">
          <Link to="/" className="nav-link">Homepage</Link>
          <Link to="/education" className="nav-link">Education</Link>
          <Link to="/experience" className="nav-link">Experience</Link>
          <Link to="/skills" className="nav-link">Skills</Link>
          <Link to="/certifications" className="nav-link">Certifications</Link>
          <Link to="/portfolio" className="nav-link">Portfolio</Link>
        </div>
      </div>
    </nav>
  );
}


function Hero() {
  return (
    <section className="hero">
      <div className="hero-overlay"></div>
      <div className="container hero-content">
        <div className="hero-text">
          <img src="/images/professional-logo.jpg" className="hero-logo" />
          <h1 className="hero-title">Welcome to my Portfolio</h1>
          <p className="hero-description">
            As a 4th year BS Computer Science student specializing in Data Science,
            I aim to create impact using data-driven insights.
          </p>
        </div>
      </div>
    </section>
  );
}

function About() {
  return (
    <section className="about-section" id="education">
      <div className="container">
        <h2 className="section-title">About Me</h2>
        <p>
          I am a Data Science student passionate about solving real-world
          problems using data and technology.
        </p>
      </div>
    </section>
  );
}

const sdgs = [
  "No Poverty","Zero Hunger","Good Health","Quality Education","Gender Equality",
  "Clean Water","Affordable Energy","Decent Work","Industry Innovation",
  "Reduced Inequalities","Sustainable Cities","Responsible Consumption",
  "Climate Action","Life Below Water","Life on Land","Peace & Justice","Partnerships"
];

const sampleProjects = [
  { title: "Education Dashboard", sdg: "Quality Education", github: "https://github.com" },
  { title: "Climate Tracker", sdg: "Climate Action", github: "https://github.com" }
];

function SDGPortfolio() {
  const [selected, setSelected] = useState<string | null>(null);

  const filtered = selected
    ? sampleProjects.filter((p) => p.sdg === selected)
    : [];

  return (
    <section className="container" id="portfolio">
      <h2>Projects by SDG</h2>

      <div className="sdg-grid">
        {sdgs.map((goal) => (
          <button key={goal} onClick={() => setSelected(goal)}>
            {goal}
          </button>
        ))}
      </div>

      {selected && (
        <div className="project-grid">
          {filtered.length > 0 ? (
            filtered.map((p, i) => (
              <div key={i} className="card">
                <h3>{p.title}</h3>
                <p>{p.sdg}</p>
                <a href={p.github} target="_blank">GitHub</a>
              </div>
            ))
          ) : (
            <p>No projects yet.</p>
          )}
        </div>
      )}
    </section>
  );
}

function Footer() {
  return (
    <footer className="footer">
        <div className="container">
            <div className="footer-content">
                <div className="footer-info">
                    <h3 className="footer-title">Earl Tan's Portfolio</h3>
                    <p className="footer-description">
                        Computer Science Student | Data Science Specialist | Aspiring Data Scientist
                    </p>
                </div>
                <div className="footer-links">
                    <a href="index.html">Home</a>
                    <a href="education.html">Education</a>
                    <a href="experience.html">Experience</a>
                    <a href="skills.html">Skills</a>
                    <a href="certifications.html">Certifications</a>
                    <a href="advocacy.html">Advocacy</a>
                    <a href="portfolio.html">Portfolio</a>
                </div>
                <div className="footer-social">
                    <a href="https://github.com" aria-label="GitHub">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                        </svg>
                    </a>
                    <a href="https://linkedin.com" aria-label="LinkedIn">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
                        </svg>
                    </a>
                    <a href="mailto:tanearl2005@gmail.com" aria-label="Email">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <rect x="2" y="4" width="20" height="16" rx="2"/>
                            <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>
                        </svg>
                    </a>
                </div>
            </div>
            <div className="footer-bottom">
                <p>&copy; 2025 Earl Tan. All rights reserved.</p>
            </div>
        </div>
    </footer>
  );
}

export default function App() {
  return (
    <>
      <Navbar />

            <Routes>
              <Route path="/" element={<Home />} />

        <Route
          path="/"
          element={
            <>
              <Hero />
              <About />
              <SDGPortfolio />
            </>
          }
        />
        <Route path="/education" element={<Education />} />
      </Routes>
      <Footer />
    </>
  );
}
