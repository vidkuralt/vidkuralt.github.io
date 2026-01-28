# CSV Viewer Pro - Progressive Web App

A beautiful, modern CSV viewer with Progressive Web App capabilities. View, sort, and manage CSV files with an elegant dark-themed interface.

## ✨ Features

### Core Features
- **Drag & Drop Import**: Simply drag CSV files onto the interface
- **File Browser**: Click to browse and select CSV files
- **Column Sorting**: Click column headers to sort (ascending → descending → original)
- **Copy to Clipboard**: Click any cell to instantly copy its value
- **Live Statistics**: Real-time display of rows, columns, and file size

### Progressive Web App Features
- **Installable**: Install as a native app on Windows, Mac, Linux, iOS, and Android
- **Offline Support**: Works without internet connection after first load
- **Fast Loading**: Cached resources for instant startup
- **Auto-Updates**: Automatically updates to the latest version
- **Desktop Integration**: Runs in its own window like a native app
- **Cross-Platform**: Works on all modern devices and operating systems

## 🚀 Installation

### Method 1: Install as Progressive Web App (Recommended)

#### On Desktop (Chrome/Edge):
1. Open `csv-viewer.html` in Chrome or Edge browser
2. Look for the install button in the address bar (⊕ icon) or click the "Install App" button that appears
3. Click "Install" in the dialog
4. The app will open in its own window and be added to your Start Menu/Applications

#### On Mobile (iOS):
1. Open `csv-viewer.html` in Safari
2. Tap the Share button
3. Select "Add to Home Screen"
4. Tap "Add"

#### On Mobile (Android):
1. Open `csv-viewer.html` in Chrome
2. Tap the menu (⋮)
3. Select "Install app" or "Add to Home Screen"
4. Tap "Install"

### Method 2: Use in Browser
Simply open `csv-viewer.html` in any modern web browser (Chrome, Edge, Firefox, Safari).

## 📖 How to Use

### Import CSV File
1. **Drag & Drop**: Drag a CSV file from your file explorer onto the drop zone
2. **Click to Browse**: Click the drop zone or "Import CSV" button to select a file

### Navigate Data
- **Scroll**: Use mouse wheel or scrollbars to navigate large datasets
- **View Statistics**: Check the stats bar for row count, column count, and file size

### Sort Columns
1. Click any column header to sort by that column
2. First click: Sort ascending (↑)
3. Second click: Sort descending (↓)
4. Third click: Return to original order

### Copy Data
- Click any cell to copy its contents to your clipboard
- A notification will appear confirming the copy action

### Clear Data
- Click the "Clear" button to reset the viewer and load a new file

## 🎨 Design Features

- **Modern Dark Theme**: Easy on the eyes with a sophisticated color palette
- **Animated Gradients**: Subtle background animations for visual appeal
- **Smooth Transitions**: Polished hover effects and micro-interactions
- **Custom Typography**: Beautiful font pairings (DM Serif Display + IBM Plex Mono)
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## 🔧 Technical Details

### Technologies Used
- **HTML5**: Semantic markup with PWA support
- **CSS3**: Modern styling with animations and gradients
- **JavaScript**: Vanilla JS for optimal performance
- **PapaParse**: Robust CSV parsing library
- **Service Worker**: Offline functionality and caching
- **Web Manifest**: PWA configuration and metadata

### File Structure
```
csv-viewer-pro/
├── csv-viewer.html      # Main application file
├── manifest.json        # PWA manifest configuration
├── service-worker.js    # Service worker for offline support
├── icon-192.png        # App icon (192x192)
├── icon-512.png        # App icon (512x512)
└── README.md           # This file
```

### Browser Compatibility
- ✅ Chrome 90+
- ✅ Edge 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Opera 76+

### PWA Features Support
- ✅ Installable on all platforms
- ✅ Offline functionality
- ✅ App icons and splash screens
- ✅ Standalone display mode
- ✅ Service worker caching
- ✅ Auto-update capability

## 🔒 Privacy & Security

- **No Server Required**: All processing happens locally in your browser
- **No Data Upload**: Your CSV files never leave your device
- **No Tracking**: No analytics or tracking scripts
- **Secure**: Uses standard web security practices

## 💡 Tips & Tricks

1. **Large Files**: The app can handle large CSV files, but performance depends on your device
2. **Offline Use**: After first load, the app works completely offline
3. **Keyboard Shortcuts**: Use Ctrl+C (Cmd+C on Mac) after clicking a cell for alternative copying
4. **Multiple Windows**: Install the app to open multiple CSV files in separate windows

## 🐛 Troubleshooting

### App won't install
- Ensure you're using a supported browser (Chrome, Edge, Safari)
- Try accessing the file through a local web server instead of file:// protocol
- Check that JavaScript is enabled

### CSV not loading
- Verify the file is a valid CSV format
- Check that the file isn't corrupted
- Try a smaller file to test functionality

### Sorting not working
- Ensure the CSV has headers in the first row
- Try clicking the column header again
- Refresh the page and reload the file

## 🆕 Future Enhancements

Potential features for future versions:
- Export filtered/sorted data
- Column filtering and search
- Data visualization (charts/graphs)
- Multiple file comparison
- Advanced sorting (multi-column)
- Custom themes
- Excel file support
- Data editing capabilities

## 📝 License

This project is open source and available for personal and commercial use.

## 🤝 Support

For issues or questions, please ensure:
1. You're using a modern browser
2. JavaScript is enabled
3. The CSV file is properly formatted
4. You have sufficient device memory for large files

---

**Enjoy using CSV Viewer Pro!** 🎉

Made with ♥ for data enthusiasts everywhere.
