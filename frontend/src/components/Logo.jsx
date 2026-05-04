export default function Logo({ size = 36, showText = true, textColor = "text-white", variant = "dark" }) {
  // variant "dark"  → sobre fondo oscuro (navbar): rect blanco semitransparente
  // variant "light" → sobre fondo blanco (login):  rect azul primario
  const rectFill   = variant === "dark" ? "rgba(255,255,255,0.18)" : "#0f4c81"
  const crossColor = variant === "dark" ? "white" : "#00b4d8"
  const pulseColor = variant === "dark" ? "rgba(255,255,255,0.5)" : "rgba(255,255,255,0.6)"

  return (
    <div className="flex items-center gap-2.5">
      <svg width={size} height={size} viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="40" height="40" rx="10" fill={rectFill}/>
        <rect x="17" y="8" width="6" height="24" rx="3" fill={crossColor}/>
        <rect x="8" y="17" width="24" height="6" rx="3" fill={crossColor}/>
        <path
          d="M8 20 L12 20 L14 15 L16 25 L18 18 L20 20 L32 20"
          stroke={pulseColor}
          strokeWidth="1.6"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
      </svg>

      {showText && (
        <span className={`text-2xl font-bold tracking-wide ${textColor}`}>
          Medi<span className="text-accent">Clinic</span>
        </span>
      )}
    </div>
  )
}
