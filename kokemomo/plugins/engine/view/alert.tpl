% for alert in values['alerts']:
    % if 'error' in alert and values['error'].have('url'):
        <label class="error">{{values['error'].get('url')['message']}}</label>
    % end
% end
