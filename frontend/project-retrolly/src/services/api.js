import axios from 'axios';

export const getProjects = projectDescription => (
	axios.post('http://127.0.0.1:5000/projects?project_description='+projectDescription)
	.then(res => res.data)
);