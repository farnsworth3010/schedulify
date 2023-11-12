import { useColorScheme } from "../../hooks/useColorScheme"
import Toggle from "react-toggle";
import "react-toggle/style.css" 
const DarkThemeToggle = () => {
    const { isDark, setIsDark } = useColorScheme()
    return(
    <Toggle
        checked={isDark}
        onChange={(e) => setIsDark(e.target.checked)}
        icons={{ checked: "🌙", unchecked: "🔆" }}
        aria-label="Dark mode toggle"
    />)
}
export default DarkThemeToggle