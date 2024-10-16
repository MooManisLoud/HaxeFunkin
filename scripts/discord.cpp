#include <iostream>
#include "discord_rpc.h"

int main()
{
    DiscordEventHandlers handlers;
    memset(&handlers, 0, sizeof(handlers));
    Discord_Initialize("1059883568811217046", &handlers, 1, NULL);

    DiscordRichPresence presence;
    memset(&presence, 0, sizeof(presence));
    presence.state = "Playing";
    presence.details = "My Game";
    presence.largeImageKey = "image_key";
    presence.largeImageText = "My Game";

    Discord_UpdatePresence(&presence);
    Discord_Shutdown();
    return 0;
}
