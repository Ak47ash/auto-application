import { Card, CardContent, Typography } from '@mui/material';

function DetailsCard({ name, mobile, email }) {
    return (
        <Card sx={{ maxWidth: 345 }}>
            <CardContent>
                <Typography gutterBottom variant="h5" component="div">
                    {name}
                </Typography>
                <Typography variant="body1" color="text.secondary">
                    {mobile}
                </Typography>
                <Typography variant="body1" color="text.secondary">
                    {email}
                </Typography>
            </CardContent>
        </Card>
    );
}

export default DetailsCard;
