import React, { useState } from "react";
import Container from '@material-ui/core/Container';
import { Typography, Box } from "@material-ui/core";
import Button from '@material-ui/core/Button';
import Divider from '@material-ui/core/Divider';

import QuickView from './QuickView';
import Settings from './Settings';
import ScheduledPickups from './ScheduledPickups';
import { OrganizationType } from '../../types/OrganizationType';
import Header from '../Header';

const styles = {
  container: {
    display: "flex",
    padding: "100px",
    paddingTop: "120px",
  },
}

export type Props = {
  location: {
    state: {
      organization: OrganizationType;
    };
  };
}

const OrganizationProfilePage: React.FC<Props> = (props: Props) => {
  const [page, setPage] = useState<string>("quick_view");

  const variant = (pageName: string) => page === pageName ? "outlined" : undefined;
  const color = (pageName: string) => page === pageName ? "primary" : undefined;
  

  return (
    <>
    <Header isWhiteBackground={true}/>
    <Container maxWidth="lg" style={styles.container}>
      <Box>
        {/* todo: set props for organization */}
        <Typography variant="h1" color="primary">Your Profile</Typography>
        <Button
          variant={variant("quick_view")}
          color={color("quick_view")}
          size="large"
          style={{"display": "inline-block"}}
          onClick={() => setPage("quick_view")}
        >
          Quick View
        </Button>
        <Button
          variant={variant("scheduled_pickups")}
          color={color("scheduled_pickups")}
          size="large"
          style={{"display": "inline-block"}}
          onClick={() => setPage("scheduled_pickups")}
        >
          Scheduled Pickups
        </Button>
        <Button
          variant={variant("settings")}
          color={color("settings")}
          size="large"
          style={{"display": "inline-block"}}
          onClick={() => setPage("settings")}
        >
          Settings
        </Button>
        <Divider style={{"width": "800px"}}/>
        {page === "quick_view" && <QuickView />}
        {page === "scheduled_pickups" && <ScheduledPickups/>}
        {page === "settings" && <Settings/>}
      </Box>
    </Container>
    </>
  );
}


export default OrganizationProfilePage

