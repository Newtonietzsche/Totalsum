#!/bin/bash

# Want to test and install the 
check_and_install_module() {
    module=$1
    if ! python3 -c "import $module" &> /dev/null; then
        echo "Module $module non trouvé. Installation..."
        pip install $module
    else
        echo "Module $module est déjà installé."
    fi
}

modules=("flask" "requests"  "langchain" "langchain_core" "langchain_openai" "PyPDF2" "reportlab" "pydub" "pyttsx3" "gTTS" "numpy")


for module in "${modules[@]}"; do
    check_and_install_module $module
done

# Test for deep translator specifically
!pip install -U deep-translator
if ! python3 -c "import deep-translator" &> /dev/null; then
    echo "Module deep-translator non trouvé. Installation..."
    pip install -U deep-translator
else
    echo "Module -U deep-translator est déjà installé."
fi


# Launch the server
python3 server.py &

# Waiting for the server
sleep 1

# open default page
xdg-open http://127.0.0.1:5001/ &
# Use the app
wait
