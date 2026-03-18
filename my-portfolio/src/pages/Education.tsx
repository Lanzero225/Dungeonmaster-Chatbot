export default function Education() {
  return (
    <>
      {/* Page Header */}
      <section className="page-header">
        <div className="container">
          <h1 className="page-title">Education</h1>
          <p className="page-description">
            My academic journey has provided me with a strong foundation in computer science and data science.
          </p>
        </div>
      </section>

      {/* Content */}
      <section className="content-section">
        <div className="container">
          <h2>Formal Education</h2>

          <div className="timeline">
            <div className="timeline-item">
              <h3>
                BS Computer Science (Data Science)
              </h3>
              <p>FEU Institute of Technology</p>
              <span>2022 - 2026</span>

              <ul>
                <li>Top Performing Student</li>
                <li>Director for Publications - ACM</li>
              </ul>
            </div>

            <div className="timeline-item">
              <h3>STEM Senior High</h3>
              <p>FEU Senior High School</p>
              <span>2020 - 2022</span>

              <ul>
                <li>With High Honors</li>
                <li>Merit Award</li>
              </ul>
            </div>
          </div>
        </div>
      </section>
    </>
  );
}