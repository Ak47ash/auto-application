// components/Navbar.js

import Link from 'next/link';
import { useState } from 'react';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Button from '@mui/material/Button';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import {signIn, signOut, useSession} from "next-auth/react";
import {Avatar, Typography} from "@mui/material";

function Navbar() {
    const { data: session } = useSession()
    console.log(`Session: ${JSON.stringify(session)} `)
    const [anchorEl, setAnchorEl] = useState(null);

    const handleMenuOpen = (event) => {
        setAnchorEl(event.currentTarget);
    };

    const handleMenuClose = () => {
        setAnchorEl(null);
    };

    const handleViewProfile = () => {
        // handle view profile logic here
        // for example, redirecting to user's profile page
    };


    return (
        <AppBar position="static">
            <Toolbar>
                <Typography variant="h6" sx={{ flexGrow: 1 }}>
                    <Link href="/">
                        Automate Jobs
                    </Link>
                </Typography>
                <Link href="/about" passHref>
                    <Button color="inherit">About</Button>
                </Link>
                {session ? (
                    <div>
                        <Button color="inherit" onClick={handleMenuOpen}>
                            <Avatar src={session.user.image} alt={session.user.name} sx={{ marginRight: '5px' }} />
                            <span>{session.user.name}</span>
                        </Button>
                        <Menu
                            anchorEl={anchorEl}
                            open={Boolean(anchorEl)}
                            onClose={handleMenuClose}
                        >
                            <MenuItem onClick={handleViewProfile}>View Profile</MenuItem>
                            <MenuItem onClick={signOut}>Logout</MenuItem>
                        </Menu>
                    </div>
                ) : (
                    <>
                    {/*<Link href="/components/login/login">Login</Link>*/}
                    <Button onClick={signIn} color="inherit">Login</Button>
                    </>
                )}
            </Toolbar>
        </AppBar>
    );
}

export default Navbar;
