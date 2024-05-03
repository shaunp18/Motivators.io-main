import React from 'react';
import './SettingsPage.scss';

const SettingsPage: React.FC = () => {
  // Implement state and handlers as needed, using useState, useEffect, etc.

  return (
    <div className="settingsPage">
      <h2>Account Settings</h2>
      <div className="settingsSection">
        <h3>Name & Image</h3>
        <p>Logged in as Royian Chowdhury</p>
        <div className="nameSection">
          <div className="initials">RC</div>
          <label htmlFor="name">Name</label>
          <input id="name" type="text" defaultValue="Royian Chowdhury" />
          <button>Save Name</button>
        </div>
        <div className="profileImageSection">
          <label>Profile Image</label>
          <div className="imageUpload">Drag and drop or Click to add image</div>
        </div>
      </div>
      <div className="settingsSection">
        <h3>Email</h3>
        <p>Your email is royian.chowdhury27@gmail.com</p>
        <p>You are logged in with your Google account. To change email, create a password for this account by resetting it <a href="#">here</a>.</p>
      </div>
      <div className="settingsSection">
        <h3>Password</h3>
        <p>You haven’t created a password yet. You can create a password by resetting it <a href="#">here</a>.</p>
      </div>
      <div className="settingsSection">
        <h3>Notifications</h3>
        <p>You are receiving emails with the results after each presentation.</p>
      </div>
      <div className="settingsSection">
        <h3>AI Tools</h3>
        <p>AI features are disabled for this account.</p>
      </div>
      <div className="settingsSection">
        <h3>Background</h3>
        <p>You're using a light background.</p>
      </div>
      <div className="logoutSection">
        <button>Log out everywhere else</button>
        <p>This will log you out from all other devices you have used Mentimeter on, for example other browsers, the PowerPoint plugin, or your mobile device.</p>
      </div>
      <div className="deleteAccountSection">
        <button>Delete Account</button>
        <p>Your account will be permanently deleted. Are you sure?</p>
      </div>
    </div>
  );
};

export default SettingsPage;
