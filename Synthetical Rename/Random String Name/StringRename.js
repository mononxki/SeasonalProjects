const fs = require('fs');
const path = require('path');
const readline = require('readline');

const currentPath = process.cwd();
let inputClosed = false;


function generateRandomName(length) {
    const characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    let result = '';
    for (let i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    return result;
}

function listSubfolders() {
    fs.readdir(currentPath, (err, files) => {
        if (err) {
            console.error(err);
            return;
        }

        const folders = files.filter(file => fs.statSync(file).isDirectory());
        if (folders.length === 0) {
            console.log('No subfolders found in the current directory.');
            return;
        }

        console.log('Subfolders in the current directory:');
        folders.forEach((folder, index) => {
            console.log(`${index + 1} - ${folder}`);
        });

        selectFolder(folders);
    });
}

function selectFolder(folders) {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question('Enter the number of the folder to rename files in: ', (selected) => {
        if (inputClosed) {
            rl.close();
            return;
        }

        const selectedFolderIndex = parseInt(selected) - 1;

        if (selectedFolderIndex >= 0 && selectedFolderIndex < folders.length) {
            console.log('Folder chosen');
            inputClosed = true; // Disable further user input
            enterAndRenameFolder(folders[selectedFolderIndex]);
        } else {
            console.log('Invalid folder number. Please enter a valid number.');
            selectFolder(folders);
        }
    });
}

function enterAndRenameFolder(folderName) {
    const folderPath = path.join(currentPath, folderName);

    fs.readdir(folderPath, (err, files) => {
        if (err) {
            console.error(err);
            return;
        }

        files.forEach(file => {
            const extension = path.extname(file);
            const newFileName = generateRandomName(8) + extension;
            const oldFilePath = path.join(folderPath, file);
            const newFilePath = path.join(folderPath, newFileName);

            fs.rename(oldFilePath, newFilePath, (err) => {
                if (err) {
                    console.error(err);
                } else {
                    console.log(`Changed ${file} to ${newFileName}`);
                }
            });
        });

        console.log(`Files in "${folderName}" have been renamed with random names.`);
    });
}

listSubfolders();
