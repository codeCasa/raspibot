using System;
using Rg.Plugins.Popup.Services;

namespace Raspibot
{
	public partial class MainPage
	{
	    private readonly HelpView _helpView;

		public MainPage()
		{
			InitializeComponent();
            _helpView = new HelpView();
		}

	    private async void ConnectButton_OnClicked(object sender, EventArgs e)
	    {
	        await Navigation.PushAsync(new RaspiPage());
	    }

	    private async void HelpButton_OnClicked(object sender, EventArgs e)
	    {
	        await PopupNavigation.Instance.PushAsync(_helpView);
	    }
	}
}
