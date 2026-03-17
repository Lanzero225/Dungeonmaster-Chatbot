import { useState } from "react";
import { projects } from "./projects.js";

const sdgs = [
  "No Poverty","Zero Hunger","Good Health","Quality Education","Gender Equality",
  "Clean Water","Affordable Energy","Decent Work","Industry Innovation",
  "Reduced Inequalities","Sustainable Cities","Responsible Consumption",
  "Climate Action","Life Below Water","Life on Land","Peace & Justice","Partnerships"
];


export default function Portfolio() {
  const [selected, setSelected] = useState<string | null>(null);

  const filtered = selected
    ? projects.filter((p) => p.sdg === selected)
    : [];

  return (
    <div style={{fontFamily:"Arial", padding:"40px", background:"#f5f5f5", minHeight:"100vh"}}>

      {/* Hero */}
      <section style={{marginBottom:"60px"}}>
        <h1 style={{fontSize:"42px"}}>Your Name</h1>
        <p style={{fontSize:"18px", maxWidth:"600px"}}>
          Data Analyst / Developer passionate about building projects aligned with the UN Sustainable Development Goals.
        </p>

        <div style={{marginTop:"20px", display:"flex", gap:"10px"}}>
          <a
            href="https://github.com"
            target="_blank"
            style={{
              padding:"10px 16px",
              border:"1px solid #333",
              borderRadius:"6px",
              textDecoration:"none"
            }}
          >
            GitHub
          </a>

          <button
            style={{
              padding:"10px 16px",
              border:"1px solid #333",
              borderRadius:"6px",
              background:"white",
              cursor:"pointer"
            }}
          >
            Contact
          </button>
        </div>
      </section>

      {/* SDG Section */}
      <section>

        <h2 style={{fontSize:"28px", marginBottom:"20px"}}>
          Projects by Sustainable Development Goals
        </h2>

        <div
          style={{
            display:"grid",
            gridTemplateColumns:"repeat(auto-fill, minmax(140px,1fr))",
            gap:"10px",
            marginBottom:"30px"
          }}
        >
          {sdgs.map((goal) => (
            <button
              key={goal}
              onClick={() => setSelected(goal)}
              style={{
                padding:"10px",
                borderRadius:"6px",
                border:"1px solid #ccc",
                background: selected === goal ? "#333" : "white",
                color: selected === goal ? "white" : "black",
                cursor:"pointer"
              }}
            >
              {goal}
            </button>
          ))}
        </div>

        {/* Projects */}
        {selected && (
          <div
            style={{
              display:"grid",
              gridTemplateColumns:"repeat(auto-fill, minmax(250px,1fr))",
              gap:"20px"
            }}
          >
            {filtered.length > 0 ? (
              filtered.map((p, i) => (
                <div
                  key={i}
                  style={{
                    border:"1px solid #ddd",
                    borderRadius:"8px",
                    padding:"20px",
                    background:"white"
                  }}
                >
                  <h3>{p.title}</h3>
                  <p style={{color:"#777"}}>{p.sdg}</p>

                  <a
                    href={p.github}
                    target="_blank"
                    style={{
                      display:"inline-block",
                      marginTop:"10px",
                      padding:"8px 12px",
                      border:"1px solid #333",
                      borderRadius:"6px",
                      textDecoration:"none"
                    }}
                  >
                    View on GitHub
                  </a>
                </div>
              ))
            ) : (
              <p>No projects yet for this SDG.</p>
            )}
          </div>
        )}
      </section>

    </div>
  );
}