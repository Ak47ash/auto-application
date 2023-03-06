// pages/about.js

import Head from 'next/head';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import DetailsCard from "@/pages/components/card/developer_card";
import {Box, Grid} from "@mui/material";

function About() {

    const details = [
        {
            id: 1,
            name: 'John Doe',
            age: 30,
            degree: 'Bachelor of Science',
            mobile: '123-456-7890',
            email: 'johndoe@example.com',
        },
        {
            id: 2,
            name: 'Jane Doe',
            age: 28,
            degree: 'Bachelor of Arts',
            mobile: '098-765-4321',
            email: 'janedoe@example.com',
        },
        {
            id: 3,
            name: 'Bob Smith',
            age: 35,
            degree: 'Master of Science',
            mobile: '555-555-5555',
            email: 'bobsmith@example.com',
        },
        {
            id: 4,
            name: 'Bob Smith',
            age: 35,
            degree: 'Master of Science',
            mobile: '555-555-5555',
            email: 'bobsmith@example.com',
        },
    ];

    return (
        <>
            <Head>
                <title>About | My Next.js App</title>
            </Head>
            <Container
                maxWidth="md"
                sx={{
                    marginTop: 4,
                    marginBottom: 4,
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                }}
            >
                <Typography
                    variant="h3"
                    component="h1"
                    sx={{
                        fontWeight: 'bold',
                        marginBottom: 2,
                    }}
                >
                    About Us
                </Typography>
                <Typography variant="body1" sx={{ textAlign: 'center' }}>
                    We are a small team of developers building awesome apps with Next.js.
                </Typography>


                <Box sx={{ p: 2 }}>
                    <Typography variant="h5" gutterBottom>
                        Details
                    </Typography>
                    <Box sx={{ mb: 2 }}>
                        <Grid container spacing={4}>
                            {details.map((detail) => (
                                <Grid item xs={12} sm={6} md={6} key={detail.id}>
                                    <DetailsCard
                                        name={detail.name}
                                        mobile={detail.mobile}
                                        email={detail.email}
                                    />
                                </Grid>
                            ))}
                        </Grid>
                    </Box>
                </Box>
            </Container>
        </>
    );
}

export default About;
