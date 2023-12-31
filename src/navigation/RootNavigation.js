import { StatusBar } from "react-native";
import { useTheme } from "../hooks";
import { AuthNavigation } from "./AuthNavigation";
import { AppNavigation } from "./AppNavigation";

export function RootNavigation(){
    const auth = null;
    const {darkMode, toggleTheme } = useTheme();

    return (
        <>
            <StatusBar 
            animated 
            barStyle={darkMode ? "light-content" : "dark-content"} 
            />            
            {auth ? <AppNavigation /> : <AuthNavigation />}
        </>
    );
}