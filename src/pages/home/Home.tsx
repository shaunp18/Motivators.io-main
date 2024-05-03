import { Radar, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis,  BarChart, Bar, XAxis, YAxis, CartesianGrid, Legend, ResponsiveContainer, Rectangle
} from 'recharts';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import Switch from '@mui/material/Switch';
import { green, purple } from '@mui/material/colors';
import Accordion from '@mui/material/Accordion';
import AccordionDetails from '@mui/material/AccordionDetails';
import AccordionSummary from '@mui/material/AccordionSummary';
import React, { useState } from 'react';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import { Calendar } from 'rsuite';
import 'rsuite/dist/rsuite.min.css';
import "./home.scss";
import { AccordionActions, Button } from "@mui/material";
import dashboardData from "../home/dashboardData.json";
import { DndProvider } from 'react-dnd';
import { HTML5Backend } from 'react-dnd-html5-backend';
import Draggable, { DraggableData, DraggableEvent } from 'react-draggable';


const Home: React.FC = ({ darkMode, toggleDarkMode }) => {
  const [draggableIconsCount1, setDraggableIconsCount1] = useState(0);
  const [draggableIconsCount2, setDraggableIconsCount2] = useState(0);
  const handleCountDraggableIcons = () => {
    // Count the number of draggable icons in box4
    const count1 = icons1.length;
    // Count the number of draggable icons in box5
    const count2 = icons2.length;


    // Update the state with the counts
    setDraggableIconsCount1(count1);
    setDraggableIconsCount2(count2);
  };
  const initialIcons1 = [
    { id: '1a', title: 'Benefits and Wellness', position: { x: 0, y: 0 } },
    { id: '2a', title: 'Building and Innovation', position: { x: 0, y: 100 } },
    { id: '3a', title: 'Career Growth and R&D', position: { x: 0, y: 200 } },
    { id: '4a', title: 'Compensation', position: { x: 0, y: 300 } },
    { id: '5a', title: 'Culture and Values', position: { x: 0, y: 400 } },
    { id: '6a', title: 'Executive Leadership', position: { x: 0, y: 500 } }
];

const initialIcons2 = [
    { id: '1b', title: 'Flexible Work', position: { x: 0, y: 0 } },
    { id: '2b', title: 'Inclusion and Social Connection', position: { x: 0, y: 100 } },
    { id: '3b', title: 'Job Security', position: { x: 0, y: 200 } },
    { id: '4b', title: 'Manager Relationship', position: { x: 0, y: 300 } },
    { id: '5b', title: 'Meaningful Work', position: { x: 0, y: 400 } },
    { id: '6b', title: 'Personal Impact', position: { x: 0, y: 500 } }
];
  const [icons1, setIcons1] = useState(initialIcons1);
  const [icons2, setIcons2] = useState(initialIcons2);


  const handleDragIcon1 = (e: DraggableEvent, ui: DraggableData, index: number) => {
    const newX = ui.x;
    const newIcons1 = [...icons1];
    if (newX < -50 || newX > 100) {
        const [removedIcon] = newIcons1.splice(index, 1);
        const iconExistsInIcons2 = icons2.some(icon => icon.id === removedIcon.id);
        if (iconExistsInIcons2) {
            setIcons1(newIcons1);
        } else {
            setIcons1(newIcons1);
            setIcons2(prevIcons2 => [...prevIcons2, { ...removedIcon, position: { x: 0, y: prevIcons2.length * 100 } }]);
        }
    } else {
        newIcons1[index] = { ...newIcons1[index], position: { x: newX, y: ui.y } };
        setIcons1(newIcons1);
    }
};


  const handleStopIcon1 = () => {
    const sortedIcons = [...icons1].sort((a, b) => a.position.y - b.position.y);
    setIcons1(sortedIcons.map((icon, index) => ({ ...icon, position: { x: 0, y: index * 100 } })));
  };


  const handleDragIcon2 = (e: DraggableEvent, ui: DraggableData, index: number) => {
    const newX = ui.x;
    const newIcons2 = [...icons2];
    if (newX < -50 || newX > 100) {
        const [removedIcon] = newIcons2.splice(index, 1);
        const iconExistsInIcons1 = icons1.some(icon => icon.id === removedIcon.id);
        if (iconExistsInIcons1) {
            setIcons2(newIcons2);
        } else {
            setIcons2(newIcons2);
            setIcons1(prevIcons1 => [...prevIcons1, { ...removedIcon, position: { x: 0, y: prevIcons1.length * 100 } }]);
        }
    } else {
        newIcons2[index] = { ...newIcons2[index], position: { x: newX, y: ui.y } };
        setIcons2(newIcons2);
    }
};


  const handleStopIcon2 = () => {
    const sortedIcons = [...icons2].sort((a, b) => a.position.y - b.position.y);
    setIcons2(sortedIcons.map((icon, index) => ({ ...icon, position: { x: 0, y: index * 100 } })));
  };
  // Define theme based on the current mode
  const theme = createTheme({
    palette: {
      mode: darkMode ? 'dark' : 'light',
      primary: {
        main: darkMode ? green[500] : purple[500],
      },
      secondary: {
        main: darkMode ? green[500] : purple[500],
      },
      text: {
        primary: darkMode ? '#fff' : '#000', // Adjust text color based on mode
      },
      background: {
        default: darkMode ? '#000' : '#fff', // Adjust background color based on mode
      },
    },
  });
  const motivators = dashboardData.motivators;
  const data = dashboardData.data;


  return (
    <DndProvider backend={HTML5Backend}>
    <ThemeProvider theme={theme}>
    <div className={`home ${darkMode ? 'dark-mode' : 'light-mode'}`}>
  <div className="box">
      <ResponsiveContainer >
        <BarChart
          layout="vertical" // This makes the chart horizontal
          data={data}
          margin={{
            top: 5,
            right: 30,
            left: 20,
            bottom: 5,
          }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis type="number" tick={{ fill: theme.palette.text.primary  }} domain={[0, 5]} />
          <YAxis dataKey="name" type="category" width={100}  tick={{ fill: theme.palette.text.primary  }} /> // YAxis now represents the categories
            {/* Dynamically setting the fill color for each bar based on the data */}
          <Bar dataKey="value" fill={darkMode ? '#fff' : '#000'}  />
        </BarChart>
      </ResponsiveContainer>
    </div>
    <div className="box6">
    {/* Submit Button */}
    <div className="submit-button" style={{ marginLeft: '20px' }}>
        <button className="submit-btn" onClick={handleCountDraggableIcons}>Submit</button>
        <p>Company #1 has {draggableIconsCount1} points</p>
        <p>Company #2 has {draggableIconsCount2} points</p>
    </div>
</div>
        <div className="box1">
     
        {motivators.map((motivator, index) => (
        <Accordion key={index} defaultExpanded={index === 2}
        sx={{
          backgroundColor: theme.palette.primary.main, // Using theme color
          color: theme.palette.text.primary, // Text color
        }}>
          <AccordionSummary
            expandIcon={<ExpandMoreIcon />}
            aria-controls={`panel${index + 1}-content`}
            id={`panel${index + 1}-header`}
          >
            {motivator.title}
          </AccordionSummary>
          <AccordionDetails>
            {motivator.description}
          </AccordionDetails>
          {/* Conditionally render AccordionActions for the last item */}
          {index === 2 && (
            <AccordionActions>
              <Button>Cancel</Button>
              <Button>Agree</Button>
            </AccordionActions>
          )}
        </Accordion>
      ))}
      </div>
     
      <div className="box2">


  <ResponsiveContainer width="100%" height="100%">
    <RadarChart cx="50%" cy="50%" outerRadius="90%" data={data}>
      <PolarGrid />
      <PolarAngleAxis dataKey="name" tick={{ fill: theme.palette.text.primary }} />
      <PolarRadiusAxis angle={30} domain={[0, 5]} tick={{ fill: theme.palette.text.primary }} />
      <Radar name="You" dataKey="value" stroke="#8884d8" fill="#8884d8" fillOpacity={0.6} />
      <Radar name="Average in Corporation" dataKey="B" stroke="#82ca9d" fill="#82ca9d" fillOpacity={0.6} />
      <Legend />
    </RadarChart>
  </ResponsiveContainer>
</div>


<div className="box3" >
      <Calendar />
    </div>
   
   
    <div className='box4'>
    <div>
              <p>Company #1</p>
              <DraggableIcon icons={icons1} setIcons={setIcons1} handleDrag={handleDragIcon1} handleStop={handleStopIcon1} />
           </div>
    </div>
    <div className='box5'>
     
    <div>
      {/* Your content goes here */}
      <p>Company #2</p>
      <DraggableIcon2 icons={icons2} setIcons={setIcons2} handleDrag={handleDragIcon2} handleStop={handleStopIcon2} />
      {/* Integrate the DraggableIcon component */}


     
    </div>
    </div>
   
    {/* Light/Dark mode switch */}
    <Switch
          checked={darkMode}
          onChange={toggleDarkMode}
          color="default"
          inputProps={{ 'aria-label': 'toggle dark mode' }}
          sx={{ position: 'absolute', top: '80px', right: '60px' }}
        />        
    </div>
    </ThemeProvider>
    </DndProvider>  
  );


};
const DraggableIcon: React.FC<any> = ({ icons, setIcons1, handleDrag, handleStop }) => {
  return (
    <div style={{ position: 'relative', width: '50%', height: '700px', border: 'none' }}>
      {icons.map((icon: any, index: number) => (
        <Draggable
          key={icon.id}
          position={icon.position}
          onDrag={(e: any, ui: any) => handleDrag(e, ui, index)}
          onStop={handleStop}
        >
          <div className="draggable-icon" style={{ position: 'absolute', cursor: 'move', width: '200px', height: '70px' }}>
            <span>{icon.title}</span>
          </div>
        </Draggable>
      ))}
    </div>
  );
};
const DraggableIcon2: React.FC<any> = ({ icons, setIcons, handleDrag, handleStop }) => {
  return (
    <div style={{ position: 'relative', width: '50%', height: '700px', border: 'none' }}>
      {icons.map((icon: any, index: number) => (
        <Draggable
          key={icon.id}
          position={icon.position}
          onDrag={(e: any, ui: any) => handleDrag(e, ui, index)}
          onStop={handleStop}
        >
          <div className="draggable-icon" style={{ position: 'absolute', cursor: 'move', width: '200px', height: '70px' }}>
            <span>{icon.title}</span>
          </div>
        </Draggable>
      ))}
    </div>
  );
};
export default Home;


