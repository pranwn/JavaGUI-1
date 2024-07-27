import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Main {
    private static CardLayout cardLayout;
    private static JPanel mainPanel;

    public static void main(String[] args) {
        JFrame frame = new JFrame("Java GUI Application");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);

        cardLayout = new CardLayout();
        mainPanel = new JPanel(cardLayout);

        mainPanel.add(createLoginPage(), "Login");
        mainPanel.add(createSearchPage(), "Search");
        mainPanel.add(createUploadPage(), "Upload");

        frame.add(mainPanel);
        frame.setVisible(true);
    }

    private static JPanel createLoginPage() {
        JPanel panel = new JPanel(new GridLayout(3, 2));
        JLabel usernameLabel = new JLabel("Username:");
        JTextField usernameField = new JTextField();
        JLabel passwordLabel = new JLabel("Password:");
        JPasswordField passwordField = new JPasswordField();
        JButton loginButton = new JButton("Login");
        JButton signupButton = new JButton("Signup");

        loginButton.addActionListener(e -> {
            String username = usernameField.getText();
            String password = new String(passwordField.getPassword());
            if (username.isEmpty() || password.isEmpty()) {
                JOptionPane.showMessageDialog(panel, "Please enter both username and password");
            } else {
                cardLayout.show(mainPanel, "Search");
            }
        });
        signupButton.addActionListener(e -> JOptionPane.showMessageDialog(panel, "Signup functionality not implemented"));

        panel.add(usernameLabel);
        panel.add(usernameField);
        panel.add(passwordLabel);
        panel.add(passwordField);
        panel.add(loginButton);
        panel.add(signupButton);

        return panel;
    }

    private static JPanel createSearchPage() {
        JPanel panel = new JPanel(new BorderLayout());

        DefaultListModel<String> fileListModel = new DefaultListModel<String>();
        fileListModel.addElement("File1.java");
        fileListModel.addElement("File2.py");
        fileListModel.addElement("File3.html");
        final JList<String> fileList = new JList<String>(fileListModel);
        JTextArea fileInfoArea = new JTextArea();
        fileInfoArea.setEditable(false);

        fileList.addListSelectionListener(e -> {
            String selectedFile = fileList.getSelectedValue();
            if (selectedFile != null) {
                fileInfoArea.setText("Information about " + selectedFile + "\nFile type: " + getFileType(selectedFile));
            }
        });

        JButton uploadPageButton = new JButton("Upload Files");
        uploadPageButton.addActionListener(e -> cardLayout.show(mainPanel, "Upload"));

        panel.add(new JScrollPane(fileList), BorderLayout.CENTER);
        panel.add(new JScrollPane(fileInfoArea), BorderLayout.SOUTH);
        panel.add(uploadPageButton, BorderLayout.NORTH);

        return panel;
    }

    private static String getFileType(String fileName) {
        int extensionIndex = fileName.lastIndexOf('.');
        if (extensionIndex > 0) {
            return fileName.substring(extensionIndex + 1);
        } else {
            return "Unknown";
        }
    }

    private static JPanel createUploadPage() {
        JPanel panel = new JPanel(new BorderLayout());
        JPanel topPanel = new JPanel(new GridLayout(2, 2));
        JLabel fileNameLabel = new JLabel("File Name:");
        JTextField fileNameField = new JTextField();
        JLabel fileContentLabel = new JLabel("File Content:");
        JTextArea fileContentArea = new JTextArea();

        topPanel.add(fileNameLabel);
        topPanel.add(fileNameField);
        topPanel.add(fileContentLabel);

        JButton uploadButton = new JButton("Upload");
        uploadButton.addActionListener(e -> {
            String fileName = fileNameField.getText();
            String fileContent = fileContentArea.getText();
            if (fileName.isEmpty() || fileContent.isEmpty()) {
                JOptionPane.showMessageDialog(panel, "Please enter both file name and content");
            } else {
                JOptionPane.showMessageDialog(panel, "File " + fileName + " has been uploaded successfully");
            }
        });

        topPanel.add(fileContentArea);
        panel.add(topPanel, BorderLayout.CENTER);
        panel.add(uploadButton, BorderLayout.SOUTH);

        return panel;
    }
}