import { Link } from "react-router-dom";

export function Navbar() {
  return (
    <nav className="navbar">
      <div className="nav-container">
        <a href="#" className="nav-logo">Earl Tan Portfolio</a>
        <div className="nav-menu">
          <a href="#" className="nav-link active">Homepage</a>
          <Link to="/education" className="nav-link">
            Education
            </Link>
          <a href="#experience" className="nav-link">Experience</a>
          <a href="#skills" className="nav-link">Skills</a>
          <a href="#certifications" className="nav-link">Certifications</a>
          <a href="#portfolio" className="nav-link">Portfolio</a>
        </div>
      </div>
    </nav>
  );
}